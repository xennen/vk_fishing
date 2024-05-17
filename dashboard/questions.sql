---Топ - 5 самых популярных имен
SELECT first_name, COUNT(first_name) as count
  FROM dds.user
 GROUP BY first_name
 ORDER BY COUNT(first_name) DESC
 LIMIT 5;

---Выдать топ-3 города, в которых среднее кол-во друзей участников группы самое наибольшее
SELECT town, AVG(friends_count) AS avg_friends_count
  FROM dds.user
 GROUP BY town
 ORDER BY avg_friends_count DESC
 LIMIT 3;

---Какой город самый часто встречаемый у участников этой группы
SELECT town, count(first_name) as members_from_town
  FROM dds.user
 WHERE town <> ''
 GROUP BY 1
 ORDER BY 2 DESC
 LIMIT 1;