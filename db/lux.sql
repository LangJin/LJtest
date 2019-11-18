/*
Navicat MySQL Data Transfer

Source Server         : 本地数据库
Source Server Version : 50724
Source Host           : localhost:3306
Source Database       : lux

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2019-06-15 03:41:46
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_admin
-- ----------------------------
DROP TABLE IF EXISTS `t_admin`;
CREATE TABLE `t_admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id,自动递增',
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_admin
-- ----------------------------
INSERT INTO `t_admin` VALUES ('1', 'admin', '123456', null, null);

-- ----------------------------
-- Table structure for t_home_bigimg
-- ----------------------------
DROP TABLE IF EXISTS `t_home_bigimg`;
CREATE TABLE `t_home_bigimg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `imgpath` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of t_home_bigimg
-- ----------------------------
INSERT INTO `t_home_bigimg` VALUES ('1', '/images/headimg/1.jpg', '#', '为情怀而干杯，告别朴素的重复和一望无际的平庸', '我在灯火阑珊处', null);
INSERT INTO `t_home_bigimg` VALUES ('2', '/images/headimg/2.jpg', '#', '喜喜喜喜喜喜', '哈哈哈哈', null);
INSERT INTO `t_home_bigimg` VALUES ('3', '/images/headimg/3.jpg', '#', '喜喜喜喜喜喜', '哈哈哈哈', null);

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id,自动递增',
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=932534910 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_user
-- ----------------------------
INSERT INTO `t_user` VALUES ('932534908', 'test123', '475d245f47680dd2c152b497d787f8ae', 'b1acb4546bf420dea144e54681107621b9a31324', null);
INSERT INTO `t_user` VALUES ('932534909', 'test124', '507dd681cbbf51f1e79d80a8ce47fd49', null, null);
