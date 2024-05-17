# vk_fishing

## **Структура репозитория**
1. Выгрузить участников группы (https://vk.com/vk_fishing), в формате (user_id_vk, fullname, last_seen, contacts, friends_count, town):

    - `/data/members.csv` - csv-файл выгрузки данных из vk.
    - `/dags/dag.py` - DAG, который поставляет данные из vk в csv в одной из тасок.
    - `/dags/scripts/vk_group_members.py` - cкрипт с логикой отправки данных из vk в csv.
    - `/dags/connections/connection_manager` - скрипт с подключением к vk.
2. Загрузить все данные в Clickhouse, архитектуру бд нужно составить самостоятельно:
    - `/dags/dag.py` - DAG, который поставляет данные из csv в БД в одной из тасок.
    - `/dags/scripts/clickhouse_group_members.py` - cкрипт с логикой отправки данных в clickhouse из csv.
    - `/dags/connections/connection_manager` - скрипт с подключением к БД.
    - `/dags/scripts/sql` - SQL-скрипты с созданием таблиц и заполнением их.
3. Используя Python и SQL, создать графики:
Топ - 5 самых популярных имен
Диаграммы рассеяния - Сколько лет (Кол-во друзей)
Дать ответы на следующие вопросы:
Выдать топ-3 города, в которых среднее кол-во друзей участников группы самое наибольшее
Какой город самый часто встречаемый у участников этой группы
    - `/dashboard` - SQL-скрипты из дашборда и скриншот.
    - `/graph` - скрипт графа и скриншот.

## **Как запустить**

```
git clone https://github.com/xennen/vk_fishing.git
cd vk_fishing
docker-compose up -d
```

Получаем ACCESS TOKEN VK на [docs](https://vk.readthedocs.io/en/latest/vk-api.html#getting-access)

Заходим в [AIRFLOW](http://localhost:8080/) -> ADMIN -> VARIABLES

Добавляем переменные:
```
ACCESS_TOKEN=ВАШ ТОКЕН
CLICKHOUSE_HOST=172.17.0.1
CLICKHOUSE_PASSWORD=clickhouse_admin
CLICKHOUSE_USERNAME=clickhouse_admin
```

Открываем [DAG](http://localhost:8080/dags/load_dag) и запускаем

