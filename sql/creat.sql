drop database if exists pyfun;
create database pyfun;
use pyfun;
create table t_User
(
    userId int auto_increment primary key,
    userName varchar(20) not null
);
 
create table t_Event
(
    id int auto_increment primary key,
    site varchar(20) not null,
	moment varchar(20) not null,
	eventTime varchar(20) not null,
	event varchar(20) not null ,
	userId int not null,
	foreign key(userId) references t_User(userId) on update cascade
);