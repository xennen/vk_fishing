# vk_fishing

## **Структура репозитория**

- `/data` - csv-файл выгрузки данных из vk.
- `/dags` - DAG, который поставляет данные из vk в clickhouse.
- `/dags/connections` - скрипт с подключениями к БД и vk.
- `/dags/scripts` - Скрипты с логикой отправки данных в clickhouse из vk.
- `/dags/scripts/sql` - SQL-скрипты с созданием таблиц и заполнением их.

