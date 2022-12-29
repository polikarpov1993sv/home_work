INSERT INTO genre_list(name) 
VALUES('Рок');

INSERT INTO genre_list(name) 
VALUES('Панк-Рок');

INSERT INTO genre_list(name) 
VALUES('Поп');

INSERT INTO genre_list(name) 
VALUES('Рок-Металл');

INSERT INTO genre_list(name) 
VALUES('Хип-Хоп');

INSERT INTO executor_list(name) 
VALUES('Король и Шут');

INSERT INTO executor_list(name) 
VALUES('Металика');

INSERT INTO executor_list(name) 
VALUES('Ёрш');

INSERT INTO executor_list(name) 
VALUES('Жигало');

INSERT INTO executor_list(name) 
VALUES('Отмель');

INSERT INTO executor_list(name) 
VALUES('Сергей Жуков');

INSERT INTO executor_list(name) 
VALUES('Тимати');

INSERT INTO executor_list(name) 
VALUES('Кис-Кис');

INSERT INTO executor_list(name) 
VALUES('Ария');

INSERT INTO genre_executor_list(genre_id, executor_id) 
VALUES(4, 1);

INSERT INTO genre_executor_list(genre_id, executor_id) 
VALUES(5, 2);

INSERT INTO genre_executor_list(genre_id, executor_id) 
VALUES(4, 3);

INSERT INTO genre_executor_list(genre_id, executor_id) 
VALUES(5, 4);

INSERT INTO genre_executor_list(genre_id, executor_id) 
VALUES(3, 5);

INSERT INTO genre_executor_list(genre_id, executor_id) 
VALUES(3, 6);

INSERT INTO genre_executor_list(genre_id, executor_id) 
VALUES(1, 7);

INSERT INTO genre_executor_list(genre_id, executor_id) 
VALUES(4, 8);

INSERT INTO genre_executor_list(genre_id, executor_id) 
VALUES(5, 9);

INSERT INTO album_list(name, year_release) 
VALUES('Одинокие жирафы', 2018);

INSERT INTO album_list(name, year_release) 
VALUES('Единорог любви', 2002);

INSERT INTO album_list(name, year_release) 
VALUES('Пустить в расход', 2014);

INSERT INTO album_list(name, year_release) 
VALUES('Рокеры сдаются', 2019);

INSERT INTO album_list(name, year_release) 
VALUES('Победа над собой', 2020);

INSERT INTO album_list(name, year_release) 
VALUES('Тигриные игры', 2019);

INSERT INTO album_list(name, year_release) 
VALUES('Любовь на нитке', 2021);

INSERT INTO album_list(name, year_release) 
VALUES('Одинокие сердца', 2013);

INSERT INTO album_list(name, year_release) 
VALUES('Танцуй пока живой', 2022);

INSERT INTO joint_album_list(executor_id, album_id) 
VALUES(1, 1);

INSERT INTO joint_album_list(executor_id, album_id) 
VALUES(2, 2);

INSERT INTO joint_album_list(executor_id, album_id) 
VALUES(3, 3);

INSERT INTO joint_album_list(executor_id, album_id) 
VALUES(4, 4);

INSERT INTO joint_album_list(executor_id, album_id) 
VALUES(5, 5);

INSERT INTO joint_album_list(executor_id, album_id) 
VALUES(6, 6);

INSERT INTO joint_album_list(executor_id, album_id) 
VALUES(7, 7);

INSERT INTO joint_album_list(executor_id, album_id) 
VALUES(8, 8);

INSERT INTO joint_album_list(executor_id, album_id) 
VALUES(9, 9);

INSERT INTO track_list(name, length, album_id) 
VALUES('Моя игра', 300, 1);

INSERT INTO track_list(name, length, album_id) 
VALUES('Мир которго нет', 350, 1);

INSERT INTO track_list(name, length, album_id) 
VALUES('Мой большой интерес', 540, 2);

INSERT INTO track_list(name, length, album_id) 
VALUES('Интро', 420, 2);

INSERT INTO track_list(name, length, album_id) 
VALUES('Бызы Кин', 210, 3);

INSERT INTO track_list(name, length, album_id) 
VALUES('Мой конечный этап', 540, 3);

INSERT INTO track_list(name, length, album_id) 
VALUES('Поезд', 410, 4);

INSERT INTO track_list(name, length, album_id) 
VALUES('Игорь', 370, 4);

INSERT INTO track_list(name, length, album_id) 
VALUES('Привет Олег', 540, 5);

INSERT INTO track_list(name, length, album_id) 
VALUES('Инквизиция', 300, 5);

INSERT INTO track_list(name, length, album_id) 
VALUES('Мой меч', 240, 6);

INSERT INTO track_list(name, length, album_id) 
VALUES('Андатра', 320, 6);

INSERT INTO track_list(name, length, album_id) 
VALUES('Еще один день', 290, 7);

INSERT INTO track_list(name, length, album_id) 
VALUES('Однажды в раю', 310, 7);

INSERT INTO track_list(name, length, album_id) 
VALUES('Ужас', 380, 8);

INSERT INTO track_list(name, length, album_id) 
VALUES('Случай в сады', 230, 8);

INSERT INTO track_list(name, length, album_id) 
VALUES('Мой единсвенный друг', 300, 9);

INSERT INTO track_list(name, length, album_id) 
VALUES('Педаль', 245, 9);

INSERT INTO collection_list(name, year) 
VALUES('Новогодний сборник №1', 2012);

INSERT INTO collection_list(name, year) 
VALUES('Новогодний сборник №2', 2013);

INSERT INTO collection_list(name, year) 
VALUES('Новогодний сборник №3', 2014);

INSERT INTO collection_list(name, year) 
VALUES('Новогодний сборник №4', 2015);

INSERT INTO collection_list(name, year) 
VALUES('Новогодний сборник №5', 2016);

INSERT INTO collection_list(name, year) 
VALUES('Новогодний сборник №6', 2017);

INSERT INTO collection_list(name, year) 
VALUES('Новогодний сборник №7', 2018);

INSERT INTO collection_list(name, year) 
VALUES('Новогодний сборник №8', 2019);

INSERT INTO collection_list(name, year) 
VALUES('Новогодний сборник №9', 2020);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(1, 1);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(2, 1);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(3, 2);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(4, 2);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(5, 3);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(6, 3);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(7, 4);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(8, 4);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(9, 5);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(10, 5);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(11, 6);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(12, 6);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(13, 7);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(14, 7);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(15, 8);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(16, 8);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(17, 9);

INSERT INTO track_collection_list(track_id, collection_id) 
VALUES(18, 9);