
-- Задача 1
SELECT name, year_release FROM album_list
WHERE year_release = 2018;

-- Задача 2
SELECT name, length FROM track_list
ORDER BY length desc
limit 1;

-- Задача 3
SELECT name, length FROM track_list
WHERE length >= 210;

-- Задача 4
select name, year from collection_list
where year between 2018 and 2020;

-- Задача 5
select name from executor_list
where name not like '% %';

-- Задача 6

select name, length from track_list
where name like '%Мой%';