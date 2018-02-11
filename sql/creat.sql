drop database if exists pyfun;
create database pyfun;
use pyfun;
CREATE TABLE `t_User` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `user_name` varchar(20) NOT NULL DEFAULT '' COMMENT '用户名称',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
CREATE TABLE `t_Event` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `site` varchar(20) NOT NULL DEFAULT '' COMMENT '地点',
  `moment` varchar(20) NOT NULL DEFAULT '' COMMENT '时刻',
  `event_time` varchar(20) NOT NULL DEFAULT '' COMMENT '事件事件',
  `event` varchar(20) NOT NULL DEFAULT '' COMMENT '事件',
  `user_id` int(11) NOT NULL COMMENT '用户id',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `t_event_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `t_User` (`user_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `t_Site` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `city` varchar(20) NOT NULL DEFAULT '' COMMENT '城市',
  `spot_code1` varchar(20) NOT NULL DEFAULT '' COMMENT '地点代码1',
  `spot_name1` varchar(20) NOT NULL DEFAULT '' COMMENT '地点名称1',
  `spot_code2` varchar(20) DEFAULT NULL COMMENT '地点代码2',
  `spot_name2` varchar(20) DEFAULT NULL COMMENT '地点名称2',
  `spot_code3` varchar(20) DEFAULT NULL COMMENT '地点代码3',
  `spot_name3` varchar(20) DEFAULT NULL COMMENT '地点名称3',
  `spot_code4` varchar(20) DEFAULT NULL COMMENT '地点代码4',
  `spot_name4` varchar(20) DEFAULT NULL COMMENT '地点名称4',
  `spot_code5` varchar(20) DEFAULT NULL COMMENT '地点代码5',
  `spot_name5` varchar(20) DEFAULT NULL COMMENT '地点名称5',
  `event` varchar(20) DEFAULT NULL COMMENT '事件',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

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