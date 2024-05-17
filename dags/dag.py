import logging

import pendulum
from airflow.decorators import dag, task
from airflow.models import Variable
from connections import ConnectionManager
from scripts import FromVkToCsv
from scripts import CsvToClickhouse

log = logging.getLogger(__name__)

CLICKHOUSE_USERNAME = Variable.get('CLICKHOUSE_USERNAME')
CLICKHOUSE_PASSWORD = Variable.get('CLICKHOUSE_PASSWORD')
CLICKHOUSE_HOST = Variable.get('CLICKHOUSE_HOST')
ACCESS_TOKEN = Variable.get('ACCESS_TOKEN')


@dag(
    schedule_interval='0/60 * * * *',
    start_date=pendulum.datetime(2024, 5, 15, tz="UTC"),
    catchup=False,
    tags=['staging']
    # params={"donot_pickle": "True"}
)
def load_dag():
    api = ConnectionManager.get_vk_connect(ACCESS_TOKEN)
    clickhouse_connect = ConnectionManager.get_clickhouse_connect(CLICKHOUSE_HOST, CLICKHOUSE_USERNAME, CLICKHOUSE_PASSWORD)
    
    csv_path = '/data/members_data.csv'
    click_loader = CsvToClickhouse(clickhouse_connect, csv_path, log)
    csv_loader = FromVkToCsv(api, csv_path, 'vk_fishing', log)
 
    @task(task_id="create_stg")
    def create_stg():
        click_loader.execute_query("create_database_stg.sql")
        click_loader.execute_query("drop_table_stg.sql")
        click_loader.execute_query("ddl_stg.sql")

    _create_stg = create_stg()

    @task(task_id="to_csv")
    def to_csv():
        csv_loader.members_to_scv()

    _to_csv = to_csv()

    @task(task_id="to_clickhouse")
    def to_clickhouse():
        columns = ['user_id_vk', 'fullname', 'last_seen',
                   'contacts', 'friends_count', 'town', 'age']
        click_loader.insert_into_clickhouse(columns)

    _to_clickhouse_stg = to_clickhouse()
    
    @task(task_id="create_and_insert_dds")
    def create_and_insert_dds():
        click_loader.execute_query("create_database_dds.sql")
        click_loader.execute_query("drop_table_dds.sql")
        click_loader.execute_query("ddl_dds.sql")
        click_loader.execute_query("insert_into_dds.sql")

    _create_and_insert_dds = create_and_insert_dds()

    _create_stg >> _to_csv >> _to_clickhouse_stg >> _create_and_insert_dds


_ = load_dag()
