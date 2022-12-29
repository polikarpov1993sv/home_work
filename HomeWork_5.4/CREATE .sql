CREATE TABLE IF NOT EXISTS genre_list (
    id SERIAL PRIMARY KEY,
    name VARCHAR(140) NOT NULL 
    );


CREATE TABLE IF NOT EXISTS executor_list (
    id SERIAL PRIMARY KEY,
    name VARCHAR(140) NOT NULL
    );


CREATE TABLE IF NOT EXISTS genre_executor_list (
	id SERIAL PRIMARY KEY,
	genre_id INTEGER NOT NULL REFERENCES genre_list(id),
	executor_id INTEGER NOT NULL REFERENCES executor_list(id)
    );

CREATE TABLE IF NOT EXISTS album_list (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(140) NOT NULL, 
    year_release INTEGER NOT NULL 
    );

CREATE TABLE IF NOT EXISTS joint_album_list (
	id SERIAL PRIMARY KEY,
	executor_id INTEGER NOT NULL REFERENCES executor_list(id),
    album_id INTEGER NOT NULL REFERENCES album_list(id)
    );

CREATE TABLE IF NOT EXISTS track_list (
    id SERIAL PRIMARY KEY,
    name VARCHAR(140) NOT NULL,
    length INTEGER NOT NULL,
    album_id INTEGER NOT NULL REFERENCES album_list(id)
    );   

CREATE TABLE IF NOT EXISTS collection_list (
    id SERIAL PRIMARY KEY,
    name VARCHAR(140) NOT NULL,
    year INTEGER NOT NULL
    );

CREATE TABLE IF NOT EXISTS track_collection_list (
    id SERIAL PRIMARY KEY,
    track_id INTEGER NOT NULL REFERENCES track_list(id),
    collection_id INTEGER NOT NULL REFERENCES collection_list(id)
    );