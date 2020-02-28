-- E-R模型中学生  教师   课程表的建立
use relevance;
create table stu(
id int primary key auto_increment,
姓名 varchar(30),
年龄 tinyint,
性别 char,
籍贯 varchar(128)
);

create table teacher(
id int primary key auto_increment,
姓名 varchar(30),
职称 varchar(30),
年龄 tinyint
);

create table course(
id int primary key auto_increment,
名称 varchar(30),
学分 float,
tid int,
constraint  t_fk
foreign  key (tid)
references teacher(id)
);

create table course_stu(
cid int,
sid int,
score float,
primary key(cid,sid),
constraint  c_fk
foreign  key (cid)
references course(id),
constraint  s_fk
foreign  key (sid)
references stu(id)
);

# 练习：
# 1. 使用cls表和interest查看学生对应的爱好和价格
select cls.name ,interest.hobby,interest.price from cls inner join interest on cls.name=interest.name;
# 2.查询所有班级学生信息，同事标注他们有什么兴趣爱好

# 3.查询所有兴趣爱好信息，并且标注与其对应的学生姓名
