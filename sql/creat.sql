drop database if exists pyfun;
create database pyfun;
use pyfun;
create table t_User
(
    user_id int auto_increment primary key,
    user_name varchar(20) not null
);
 
create table t_Event
(
    id int auto_increment primary key,
    site varchar(20) not null,
    moment varchar(20) not null,
    event_time varchar(20) not null,
    event varchar(20) not null ,
    user_id int not null,
    foreign key(user_id) references t_User(user_id) on update cascade
);

CREATE TABLE t_Site
(
  id INT AUTO_INCREMENT PRIMARY KEY ,
  city VARCHAR(20) NOT NULL ,
  spot_code1 VARCHAR(20)NOT NULL,
  spot_name1 VARCHAR(20)NOT NULL,
  spot_code2 VARCHAR(20),
  spot_name2 VARCHAR(20),
  spot_code3 VARCHAR(20),
  spot_name3 VARCHAR(20),
  spot_code4 VARCHAR(20),
  spot_name4 VARCHAR(20),
  spot_code5 VARCHAR(20),
  spot_name5 VARCHAR(20),
  event VARCHAR(20)
);

INSERT INTO t_Site (
  city,
  spot_code1,
  spot_name1,
  spot_code2,
  spot_name2
)
VALUES (
  '爱知县',
  'mingguwu',
  '名古屋城',
  NULL ,
  NULL
),
  (
  '兵库县',
  'youmawenquan',
  '有马温泉',
  NULL ,
  NULL
),
  (
  '大分县',
  'biefuwenquan',
  '别府温泉',
  NULL ,
  NULL
),
  (
  '京都市',
  'tianqiaoli',
  '天桥立',
  'yuzhiqiao' ,
  '宇治桥'
),
(
  '鹿儿岛',
  'shengwenshan',
  '绳文杉',
  NULL ,
  NULL
),
  (
  '青森县',
  'aorulaixiliu',
  '奥入濑溪流',
  NULL ,
  NULL
),
  (
  '秋田县',
  'rudaoqidengta',
  '入道埼灯塔',
  NULL ,
  NULL
),
  (
  '群马县',
  'caojinwenquan',
  '草津温泉',
  NULL ,
  NULL
),
  (
  '长野县',
  'xinzhoushanguangsi',
  '信州善光寺',
  NULL ,
  NULL
)