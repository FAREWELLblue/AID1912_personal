create database books character set utf8;
use books;
create table book(id int primary key auto_increment,
title varchar(30) not null ,
author varchar(30) not null,
publication varchar(50),
price float ,
comment text);

insert into class_1 values(1,'Lily',12,'w',91.5),(2,'tom',13,'m','76');

select  * from class_1;

insert into class_1 (name,age,sex,score)
values ('Jame',12,'m',90);

delete from class_1 where id=4;

update class_1 set score = 50 where name='Jame';

select * from interest;

delete from interest where id = 1;
insert into interest values (1,'Emma','sing,dance','B+',16800.00,'骨骼惊奇');