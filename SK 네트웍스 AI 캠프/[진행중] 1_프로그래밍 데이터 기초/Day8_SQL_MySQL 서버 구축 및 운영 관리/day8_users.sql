SELECT user, host FROM mysql.user;
SELECT USER(), CURRENT_USER();

CREATE USER homework IDENTIFIED BY 'Homework80*';
GRANT ALL privileges ON homework_db.* to homework;
GRANT ALL privileges ON mysql.* to homework;
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, delete TO homework;
SHOW GRANTS FOR homework;

show databases;
create database test_db;
drop database test_db;

USE MYSQL;
CREATE table STUDENT(
	ID INT primary KEY auto_increment,
    NAME VARCHAR(20),
    SCORE INT
);
show tables;

create table manage(
	market varchar(20),
    buy int, 
    sell int, 
    stock int,
    day date
);
select table_name from information_schema.tables where table_name like '%manage%';

insert into manage values
('A', 100, 120, 50, '2026-01-01'),
('B', 80, 90, 30, '2026-01-02'),
('C', 150, 160, 70, '2026-01-03');
select * from manage;

create view v_manage as select market, (sell - buy) as profit from manage;
create view v_manage as select market, (sell - buy) as profit from manage;
select * from v_manage;