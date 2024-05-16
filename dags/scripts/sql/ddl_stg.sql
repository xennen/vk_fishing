--- Создаем таблицу для сырых данных
CREATE TABLE IF NOT EXISTS stg.group_members
(
    user_id_vk VARCHAR(30),
    fullname VARCHAR(50),
    last_seen VARCHAR(30),
    contacts VARCHAR(30),
    friends_count VARCHAR(5),
    town VARCHAR(30),
    age VARCHAR (3)
)
ENGINE=MergeTree
ORDER BY user_id_vk;