insert into singers(id, nickname)
values(1, 'The Weeknd');

insert into singers(id, nickname)
values(2, 'treepside');

insert into singers(id, nickname)
values(3, 'ROCKET');

insert into singers(id, nickname)
values(4, 'Twenty one pilots');

insert into singers(id, nickname)
values(5, '3TERNITY');

insert into singers(id, nickname)
values(6, 'Mr. Kitty');

insert into singers(id, nickname)
values(7, '4n Way');

insert into singers(id, nickname)
values(8, 'Miyagi');

insert into genres(id, name)
values(1, 'Hip-hop');

insert into genres(id, name)
values(2, 'Hookah rap');

insert into genres(id, name)
values(3, 'Rap');

insert into genres(id, name)
values(4, 'Pop');

insert into genres(id, name)
values(5, 'Rock');

insert into albums(id, name, release_date)
values(1, 'Yamakasi', '17-07-2020');

insert into albums(id, name, release_date)
values(2, 'Kids see ghosts', '08-06-2018');

insert into albums(id, name, release_date)
values(3, 'world', '02-12-2022');

insert into albums(id, name, release_date)
values(4, 'SYSTEM 3RASE', '24-12-2021');

insert into albums(id, name, release_date)
values(5, 'Optic Illusion', '28-01-2022');

insert into albums(id, name, release_date)
values(6, 'Blurryface', '17-05-2015');

insert into albums(id, name, release_date)
values(7, 'The Highlights', '05-02-2021');

insert into albums(id, name, release_date)
values(8, 'Tsukuyomi Dream', '14-08-2019');

insert into albums(id, name, release_date)
values(9, 'Time', '08-07-2019');

insert into songs(id, name, time, id_of_album)
values(1, 'Blinding Lights', '3:20', 6);

insert into songs(id, name, time, id_of_album)
values(2, 'Cant" Feel My Face', '3:33', 6);

insert into songs(id, name, time, id_of_album)
values(3, 'Call Out My Name', '3:48', 6);

insert into songs(id, name, time, id_of_album)
values(4, 'Starboy', '3:50', 6);

insert into songs(id, name, time, id_of_album)
values(5, 'Stressed Out', '3:22', 5);

insert into songs(id, name, time, id_of_album)
values(6, 'Polarize', '3:45', 5);

insert into songs(id, name, time, id_of_album)
values(7, 'Hometown', '3:54', 5);

insert into songs(id, name, time, id_of_album)
values(8, 'Lane Boy', '4:13', 5);

insert into songs(id, name, time, id_of_album)
values(9, 'Yamakasi', '4:23', 1);

insert into songs(id, name, time, id_of_album)
values(10, 'Utopia', '3:29', 1);

insert into songs(id, name, time, id_of_album)
values(11, 'Infinite Tsukuyomi', '3:23', 7);

insert into songs(id, name, time, id_of_album)
values(12, 'LUV', '3:15', 7);

insert into songs(id, name, time, id_of_album)
values(13, 'дождь', '2:47', 2);

insert into songs(id, name, time, id_of_album)
values(14, 'в сети', '1:53', 2);

insert into songs(id, name, time, id_of_album)
values(15, 'Фитиль', '3:12', 3);

insert into collections(id, name, release_date)
values(1, 'Slowed', '17-11-2021');

insert into collections(id, name, release_date)
values(2, 'Go end', '09-07-2021');

insert into collections(id, name, release_date)
values(3, 'Lead', '08-10-2020');

insert into collections(id, name, release_date)
values(4, 'Fan pilots', '16-02-2018');

insert into collections(id, name, release_date)
values(5, 'Low dance', '25-04-2017');

insert into collections(id, name, release_date)
values(6, 'Today Weekend', '14-06-2020');

insert into collections(id, name, release_date)
values(7, 'Stone and shark', '12-09-2021');

insert into collections(id, name, release_date)
values(8, 'Soul of all songs', '30-10-2022');

insert into albums_and_singers(album_id, singer_id)
values(1, 8);

insert into albums_and_singers(album_id, singer_id)
values(2, 2);

insert into albums_and_singers(album_id, singer_id)
values(3, 5);

insert into albums_and_singers(album_id, singer_id)
values(4, 5);

insert into albums_and_singers(album_id, singer_id)
values(5, 4);

insert into albums_and_singers(album_id, singer_id)
values(6, 1);

insert into albums_and_singers(album_id, singer_id)
values(7, 3);

insert into albums_and_singers(album_id, singer_id)
values(8, 6);

insert into genres_and_singers(genre_id, singer_id)
values(1, 1);

insert into genres_and_singers(genre_id, singer_id)
values(1, 2);

insert into genres_and_singers(genre_id, singer_id)
values(1, 3);

insert into genres_and_singers(genre_id, singer_id)
values(1, 4);

insert into genres_and_singers(genre_id, singer_id)
values(1, 5);

insert into genres_and_singers(genre_id, singer_id)
values(2, 8);

insert into genres_and_singers(genre_id, singer_id)
values(3, 3);

insert into genres_and_singers(genre_id, singer_id)
values(3, 5);

insert into genres_and_singers(genre_id, singer_id)
values(4, 1);

insert into genres_and_singers(genre_id, singer_id)
values(4, 6);

insert into genres_and_singers(genre_id, singer_id)
values(4, 7);

insert into collections_and_songs(collection_id, song_id)
values(6, 1);

insert into collections_and_songs(collection_id, song_id)
values(6, 2);

insert into collections_and_songs(collection_id, song_id)
values(7, 2);

insert into collections_and_songs(collection_id, song_id)
values(6, 3);

insert into collections_and_songs(collection_id, song_id)
values(8, 3);

insert into collections_and_songs(collection_id, song_id)
values(4, 1);

insert into collections_and_songs(collection_id, song_id)
values(6, 14);

insert into collections_and_songs(collection_id, song_id)
values(2, 7);

insert into collections_and_songs(collection_id, song_id)
values(3, 7);

insert into collections_and_songs(collection_id, song_id)
values(1, 11);

insert into collections_and_songs(collection_id, song_id)
values(6, 11);

insert into collections_and_songs(collection_id, song_id)
values(5, 12);

insert into collections_and_songs(collection_id, song_id)
values(5, 7);

insert into collections_and_songs(collection_id, song_id)
values(4, 4);

insert into collections_and_songs(collection_id, song_id)
values(3, 13);

insert into collections_and_songs(collection_id, song_id)
values(8, 8);

insert into collections_and_songs(collection_id, song_id)
values(3, 15);





