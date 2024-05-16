--- Заполняем таблицу кастуя данные в нужный формат
INSERT INTO dds.user (user_id_vk, first_name, second_name, last_seen, age, contacts, friends_count, town)
SELECT toInt64OrNull(user_id_vk) as user_id_vk,
       splitByChar(' ', fullname)[1] AS first_name,
       splitByChar(' ', fullname)[2] AS second_name,
       toDateTime64OrNull(last_seen) as last_seen,
       toInt32OrNull(age) as age,
       contacts,
       toInt32OrNull(friends_count),
       town
  FROM stg.group_members;