# vk_fishing

## **Структура репозитория**

- `/data` - csv-файл выгрузки данных из vk.
- `/dags` - DAG, который поставляет данные из vk в clickhouse.
- `/dags/connections` - скрипт с подключениями к БД и vk.
- `/dags/scripts` - Скрипты с логикой отправки данных в clickhouse из vk.
- `/dags/scripts/sql` - SQL-скрипты с созданием таблиц и заполнением их.
- `/dashboard` - SQL-скрипты из дашборда и скриншот.
- `/graph` - скрипт графа и скриншот.

## **Как запустить**

```
git clone https://github.com/xennen/vk_fishing.git
cd vk_fishing
docker-compose up -d
```

Получаем ACCESS TOKEN VK на [vkhost.github](https://vkhost.github.io/)

Заходим в [AIRFLOW](http://localhost:8080/) -> ADMIN -> VARIABLES

Добавляем переменные:
```
ACCESS_TOKEN=ВАШ ТОКЕН
CLICKHOUSE_HOST=172.17.0.1
CLICKHOUSE_PASSWORD=clickhouse_admin
CLICKHOUSE_USERNAME=clickhouse_admin
```

Открываем [DAG](http://localhost:8080/dags/load_dag) и запускаем

