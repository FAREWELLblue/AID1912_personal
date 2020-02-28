show databases;

use books;
select * from book;
use student;
select * from sanguo;

# 练习；
# 1.统计每位作家写的图书的平均价格；
select author,avg(price) from book group by author;
# 2.统计每个出版社出版图书的数量
select publication,count(*) from book group by publication;
# 3.查看总共有多少个出版社
select count(distinct publication) from book;
# 4.筛选出那些出版的图书超过50元的图书的出版社，并按照出版图书的最高价格倒序排序
select title,publication,price from book where price>50 order by price desc ;
select publication,max(price) from book group by publication having max(price)>50 order by max(price) desc;
# 5.统计所有出版时间的图书的平均价格
select publication_time,avg(price) from book group by publication_time;

CREATE TABLE dept (id int PRIMARY KEY auto_increment,dname VARCHAR(50) not null);
CREATE TABLE `person` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `age` tinyint DEFAULT 0,
  `sex` enum('m','w','o') DEFAULT 'o',
  `salary` decimal(8,2) DEFAULT 250.00,
  `hire_date` date NOT NULL,
  `dept_id` int DEFAULT NULL
) ;
insert into dept values(1,' 技术部'),(2,'财务部'),(3,'销售部'),(4,'行政部'),(5,'市场部');
insert into person values
(1,'Lily',29,'w',20000,'2017-4-3',2),
(2,'Tom',27,'m',16000,'2019-10-3',1),
(3,'Joy',32,'m',34000,'2016-5-20',1),
(4,'Emma',29,'w',12000,'2018-7-7',4),
(5,'Baron',24,'m',15000,'2019-3-29',5),
(6,'Abby',30,'w',18000,'2018-11-3',3);
insert into person values
(7,'Jame',38,'m',40000,'2017-4-3',1),
(8,'Alex',24,'w',13000,'2018-1-21',2);

alter table person add constraint dept_fk foreign key (dept_id) references dept (id);

use relevance;
create table person(
  id varchar(32) primary key,
  name varchar(30),
  sex char(1),
  age int
);

create table car(
  id varchar(32) primary key,
  name varchar(30),
  price decimal(10,2),
  pid varchar(32),
  constraint car_fk foreign key(pid) references person(id)
);

CREATE TABLE `athlete` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `age` tinyint NOT NULL,
  `country` varchar(30) NOT NULL,
  `description` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `item` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rname` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `athlete_item` (
  `aid` int NOT NULL,
  `tid` int NOT NULL,
  PRIMARY KEY (`aid`,`tid`),
  CONSTRAINT `athlete_fk` FOREIGN KEY (`aid`) REFERENCES `athlete` (`id`),
  CONSTRAINT `item_fk` FOREIGN KEY (`tid`) REFERENCES `item` (`id`)
);
# 练习：完成朋友圈表的建设
# 用户信息cat
# 朋友圈内容
# 点赞评论内容






















