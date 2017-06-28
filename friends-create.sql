create database if not exists friendsdb
;

use friendsdb
;


drop table if exists friends
;


create table friends (
 id int auto_increment primary key, 
 first_name varchar(100),
 last_name varchar(100),
 email varchar(100),
 created_at datetime not null default current_timestamp,
 updated_at datetime not null default current_timestamp
)
;
-- add some data 
INSERT INTO friends (first_name, last_name, email) 
VALUES 
('Jay', 'Patel', 'jay@gmail.com'),
('Jimmy', 'Jun', 'jim@gmail.com')
;
