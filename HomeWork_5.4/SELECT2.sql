select name_genre,  count(executor_id) from genre_executor_list
left join genre_list on genre_executor_list.genre_id = genre_list.id
group by name_genre

select year_release, count(track_name) from album_list
left join track_list on album_list.id = track_list.album_id 
where year_release <= 2020 and year_release >= 2018
group by year_release

select album_name, avg(length) from album_list
left join track_list on album_list.id = track_list.album_id 
group by album_name

select executor_name from executor_list
left join joint_album_list on executor_list.id = joint_album_list.executor_id
left join  album_list on album_list.id = joint_album_list.album_id
where album_list.year_release != 2020

select collection_name from collection_list
left join track_collection_list on collection_list.id = track_collection_list.collection_id  
left join track_list on track_collection_list.track_id  = track_list.id 
left join album_list on track_list.album_id  = album_list.id 
left join joint_album_list on album_list.id  = joint_album_list.album_id 
left join executor_list on executor_list.id  = joint_album_list.executor_id 
where executor_name like 'Король и Шут'
group by collection_name

select album_name from album_list
left join joint_album_list on album_list.id = joint_album_list.album_id 
left join executor_list on joint_album_list.executor_id = executor_list.id 
left join genre_executor_list on executor_list.id = genre_executor_list.executor_id 
left join genre_list on genre_executor_list.genre_id = genre_list.id 
group by album_name
having count(name_genre) >1

select track_name from track_list
left join track_collection_list on track_list.id = track_collection_list.track_id
group by track_name
having count(collection_id) < 1

select executor_name, min(length) from executor_list
left join joint_album_list on executor_list.id = joint_album_list.executor_id 
left join album_list on joint_album_list.album_id = album_list.id 
left join track_list on  album_list.id = track_list.album_id 
group by executor_name
order by min(length)
limit 3

select album_name, count(track_name) from album_list
left join track_list on album_list.id = track_list.album_id
group by album_name
order by count(track_name)
limit 3



