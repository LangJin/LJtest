/*
Navicat MySQL Data Transfer

Source Server         : 本地数据库
Source Server Version : 50724
Source Host           : localhost:3306
Source Database       : ljtestdb

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2019-12-10 16:23:43
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_article
-- ----------------------------
DROP TABLE IF EXISTS `t_article`;
CREATE TABLE `t_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL COMMENT '题目',
  `content` varchar(255) DEFAULT NULL COMMENT '内容',
  `tags` varchar(255) DEFAULT NULL COMMENT '分类',
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '状态，0正常1删除',
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `uid` int(11) DEFAULT NULL COMMENT '用户id',
  `remark` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='心得体会';

-- ----------------------------
-- Records of t_article
-- ----------------------------

-- ----------------------------
-- Table structure for t_coures
-- ----------------------------
DROP TABLE IF EXISTS `t_coures`;
CREATE TABLE `t_coures` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL COMMENT '教程标题',
  `content` varchar(255) NOT NULL COMMENT '教程内容',
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '状态0正常1删除',
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `tags` varchar(255) DEFAULT NULL COMMENT '分类',
  `remark` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='教程表';

-- ----------------------------
-- Records of t_coures
-- ----------------------------

-- ----------------------------
-- Table structure for t_inspirer
-- ----------------------------
DROP TABLE IF EXISTS `t_inspirer`;
CREATE TABLE `t_inspirer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '状态 0正常 1删除',
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='灵光一闪';

-- ----------------------------
-- Records of t_inspirer
-- ----------------------------

-- ----------------------------
-- Table structure for t_questions
-- ----------------------------
DROP TABLE IF EXISTS `t_questions`;
CREATE TABLE `t_questions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL COMMENT '问题题目',
  `content` varchar(255) DEFAULT NULL COMMENT '问题内容',
  `tags` varchar(255) DEFAULT NULL COMMENT '问题分类',
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '状态 0正常1删除',
  `uid` int(11) NOT NULL COMMENT '提问人ID',
  `remark` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='交流讨论表';

-- ----------------------------
-- Records of t_questions
-- ----------------------------
INSERT INTO `t_questions` VALUES ('1', 'admi....n', '123456', '测试', null, '0', '4', null, '2019-11-19 16:45:35', '2019-11-19 16:45:39');
INSERT INTO `t_questions` VALUES ('2', 'admi....n', '123456', '测试', null, '0', '4', null, null, null);
INSERT INTO `t_questions` VALUES ('3', 'admi....n', '123456', '测试', null, '0', '4', null, null, null);
INSERT INTO `t_questions` VALUES ('4', 'admi....n', '123456', '测试', null, '0', '1', null, null, null);

-- ----------------------------
-- Table structure for t_title_img
-- ----------------------------
DROP TABLE IF EXISTS `t_title_img`;
CREATE TABLE `t_title_img` (
  `id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL COMMENT '轮播图标题',
  `content` varchar(255) DEFAULT NULL COMMENT '轮播图内容',
  `imghost` varchar(255) NOT NULL,
  `remark` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='轮播图表';

-- ----------------------------
-- Records of t_title_img
-- ----------------------------
INSERT INTO `t_title_img` VALUES ('1', '不积跬步无以至千里', '人啊就是要努力', '/images/1.jpg', null, '2019-12-10 16:16:44', '2019-12-10 16:16:44');

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL COMMENT '账号',
  `password` varchar(255) NOT NULL COMMENT '密码',
  `token` varchar(255) DEFAULT NULL COMMENT 'token',
  `nickname` varchar(255) DEFAULT NULL,
  `titlepic` varchar(255) DEFAULT NULL,
  `headpic` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `sex` varchar(255) DEFAULT NULL,
  `job` varchar(255) DEFAULT NULL COMMENT '职业',
  `email` varchar(255) DEFAULT NULL,
  `weixin` varchar(255) DEFAULT NULL,
  `QQ` varchar(255) DEFAULT NULL,
  `userinfo` varchar(255) DEFAULT NULL COMMENT '个人签名',
  `address` varchar(255) DEFAULT NULL,
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '0正常1删除2拉黑',
  `remark` varchar(255) DEFAULT NULL COMMENT '昵称',
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COMMENT='用户表';

-- ----------------------------
-- Records of t_user
-- ----------------------------
INSERT INTO `t_user` VALUES ('1', 'admin', '123456', 'b8ddd1442485fba8eb0b0a18a5fe539f9ffb26b6', null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('2', 'admi...n', '123456', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('3', 'admi.....n', '123456', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('4', 'admi....n', '123456', '5862c4550896b0090f54e309c8822df279a7f5da', null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('5', 'yujing', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('6', '123456', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('7', '123456789', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('8', '1234567', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('9', '12345678', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('10', 'yujing123456', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('11', 'yujing1234', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('12', 'yujing123', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('13', '123121212', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('15', '123456788', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('16', '12345898', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('17', 'yujing123123', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('18', 'iiii23yi', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('19', '0000000', '00000000', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
