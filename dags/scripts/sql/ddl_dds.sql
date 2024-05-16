--- Создаем одну таблицу и не нормализуем данные т.к БД не любит join's
CREATE TABLE IF NOT EXISTS dds.user
(
    user_id_vk Int64,
    first_name VARCHAR(20),
    second_name VARCHAR(20),
    last_seen DATETIME,
    age Int16,
    contacts VARCHAR(30),
    friends_count Int32,
    town VARCHAR(30)
)
ENGINE=MergeTree
PARTITION BY toYYYYMM(last_seen)
PRIMARY KEY user_id_vk
ORDER BY (user_id_vk, last_seen);