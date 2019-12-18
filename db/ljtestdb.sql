/*
Navicat MySQL Data Transfer

Source Server         : 浪晋的腾讯云
Source Server Version : 50726
Source Host           : 192.144.148.91:3306
Source Database       : ljtestdb

Target Server Type    : MYSQL
Target Server Version : 50726
File Encoding         : 65001

Date: 2019-12-18 23:54:30
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_article
-- ----------------------------
DROP TABLE IF EXISTS `t_article`;
CREATE TABLE `t_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL COMMENT '题目',
  `brief` varchar(255) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL COMMENT '内容',
  `ximg` varchar(255) NOT NULL DEFAULT '/static/images/ximg.jpg' COMMENT '图片显示',
  `tags` varchar(255) DEFAULT NULL COMMENT '分类',
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '状态，0正常1删除',
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `uid` int(11) DEFAULT NULL COMMENT '用户id',
  `goods` int(16) NOT NULL DEFAULT '0' COMMENT '点赞数量',
  `collections` int(16) NOT NULL DEFAULT '0' COMMENT '收藏数量',
  `follows` int(16) NOT NULL DEFAULT '0' COMMENT '关注数量',
  `remark` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8 COMMENT='心得体会';

-- ----------------------------
-- Records of t_article
-- ----------------------------
INSERT INTO `t_article` VALUES ('1', '测试', null, '测试真棒', '/static/images/ximg.jpg', '测试', '0', '王五', '1', '-6', '5', '0', '', '2019-12-18 23:53:25', '2019-12-18 23:53:25');
INSERT INTO `t_article` VALUES ('2', '学习测试', null, '学，学测试', '/static/images/ximg.jpg', '学习', '0', '抖音', '1', '-1', '1', '0', null, '2019-12-17 19:59:55', '2019-12-17 19:59:55');
INSERT INTO `t_article` VALUES ('3', '为什么要学习测试', null, '内容', '/static/images/ximg.jpg', '测试', '0', 'None', '56', '-2', '0', '0', null, '2019-12-18 17:02:15', '2019-12-18 17:02:15');
INSERT INTO `t_article` VALUES ('4', '', null, '内容', '/static/images/ximg.jpg', '测试', '0', 'None', '6', '0', '1', '0', null, '2019-12-18 18:41:16', '2019-12-18 18:41:16');
INSERT INTO `t_article` VALUES ('5', '', null, 'None', '/static/images/ximg.jpg', 'None', '0', 'None', '6', '0', '0', '0', null, '2019-12-17 16:44:23', '2019-12-17 16:44:23');
INSERT INTO `t_article` VALUES ('6', 'None', null, 'None', '/static/images/ximg.jpg', 'None', '0', 'None', '6', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('7', 'None', null, 'None', '/static/images/ximg.jpg', 'None', '0', 'None', '6', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('8', 'None', null, 'None', '/static/images/ximg.jpg', 'None', '0', 'None', '6', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('9', '为什么要学习测试', null, '内容', '/static/images/ximg.jpg', '测试', '0', 'None', '81', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('10', '为什么要学习测试', null, '内容', '/static/images/ximg.jpg', '测试', '0', 'None', '80', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('11', '为什么要学习测试', null, '内容', '/static/images/ximg.jpg', '测试', '0', 'None', '82', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('12', '为什么要学习测试', null, '内容', '/static/images/ximg.jpg', '测试', '0', 'None', '81', '0', '0', '0', null, '2019-12-18 15:06:33', '2019-12-18 15:06:33');
INSERT INTO `t_article` VALUES ('13', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '89', '-5', '0', '0', null, '2019-12-17 15:58:13', '2019-12-17 15:58:13');
INSERT INTO `t_article` VALUES ('14', '烟大侠的学习心路', '介绍', '告诉你们吧', '/static/images/ximg.jpg', '测试', '0', null, '82', '1', '0', '0', null, '2019-12-17 19:36:36', '2019-12-17 19:36:36');
INSERT INTO `t_article` VALUES ('15', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '1', '-4', '0', '0', null, '2019-12-17 15:40:41', '2019-12-17 15:40:41');
INSERT INTO `t_article` VALUES ('16', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '1', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('17', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '1', '1', '0', '0', null, '2019-12-17 16:35:09', '2019-12-17 16:35:09');
INSERT INTO `t_article` VALUES ('18', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '1', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('19', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '1', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('20', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '1', null, '72', '0', '0', '0', null, '2019-12-17 22:10:23', '2019-12-17 22:10:23');
INSERT INTO `t_article` VALUES ('21', 'AAAAAAAAAAAAA试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '1', null, '72', '0', '0', '0', null, '2019-12-17 22:19:51', '2019-12-17 22:19:51');
INSERT INTO `t_article` VALUES ('22', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '93', '-1', '0', '0', null, '2019-12-17 16:39:06', '2019-12-17 16:39:06');
INSERT INTO `t_article` VALUES ('23', '很久很久以前', '1', '在很远很远的地方 ', '/static/images/ximg.jpg', '有一群蓝精灵', '0', null, '82', '-2', '1', '0', null, '2019-12-17 21:50:28', '2019-12-17 21:50:28');
INSERT INTO `t_article` VALUES ('24', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '1', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('25', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '1', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('26', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '1', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('27', '不学行不行', '1', '1', '/static/images/ximg.jpg', '1', '0', null, '82', '0', '0', '0', null, '2019-12-17 22:32:15', '2019-12-17 22:32:15');
INSERT INTO `t_article` VALUES ('28', '不学', '1', '1', '/static/images/ximg.jpg', '1', '0', null, '82', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('29', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '39', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('30', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '99', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('31', '看看能不能改你', 'None', '内容', '/static/images/ximg.jpg', '测试', '0', null, '76', '0', '0', '0', null, '2019-12-17 22:14:35', '2019-12-17 22:14:35');
INSERT INTO `t_article` VALUES ('32', '钻石', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '76', '0', '0', '0', null, '2019-12-17 14:48:47', '2019-12-17 14:48:47');
INSERT INTO `t_article` VALUES ('33', '钻石', '介绍', '内容', '/static/images/ximg.jpg', '测试', '1', null, '76', '0', '0', '0', null, '2019-12-17 14:47:57', '2019-12-17 14:47:57');
INSERT INTO `t_article` VALUES ('34', '', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '56', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('35', '钻石', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '25', '0', '1', '0', null, '2019-12-17 21:51:59', '2019-12-17 21:51:59');
INSERT INTO `t_article` VALUES ('36', '', '介绍', '白银', '/static/images/ximg.jpg', '测试', '0', null, '25', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('37', '？！@#', '介绍', '白银', '/static/images/ximg.jpg', '测试', '0', null, '25', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('38', '', '介绍', '白银', '/static/images/ximg.jpg', '测试', '0', null, '25', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('39', '吃五香鸭吗，还是好吃的哟,', '介绍', '为了搞钱', '/static/images/ximg.jpg', '搞钱是人生大事', '0', null, '64', '0', '0', '0', null, '2019-12-17 22:13:50', '2019-12-17 22:13:50');
INSERT INTO `t_article` VALUES ('40', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '1', null, '64', '0', '0', '0', null, '2019-12-17 22:17:26', '2019-12-17 22:17:26');
INSERT INTO `t_article` VALUES ('41', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '105', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('42', '为什么要学习测试2', '介绍2', '内容2', '/static/images/ximg.jpg', '测试2', '0', null, '123', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('43', '为什么要学习测试1', '介绍1', '内容1', '/static/images/ximg.jpg', '测试1', '0', null, '123', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('44', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '79', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('45', '', '介绍', '', '/static/images/ximg.jpg', '测试', '1', null, '10', '0', '0', '0', null, '2019-12-18 17:08:21', '2019-12-18 17:08:21');
INSERT INTO `t_article` VALUES ('46', '', '介绍', '怎么可能告诉你们', '/static/images/ximg.jpg', '测试', '0', null, '10', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('47', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '79', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('48', '没删掉？', '介绍', '告诉你们吧', '/static/images/ximg.jpg', '测试', '1', null, '10', '0', '0', '0', null, '2019-12-17 19:48:10', '2019-12-17 19:48:10');
INSERT INTO `t_article` VALUES ('49', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '72', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('50', '', '', '', '/static/images/ximg.jpg', '', '0', null, '72', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('51', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '39', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('52', '22', '介绍123', '22', '/static/images/ximg.jpg', '222', '0', null, '131', '0', '0', '0', null, '2019-12-17 22:12:25', '2019-12-17 22:12:25');
INSERT INTO `t_article` VALUES ('53', '22', '介绍', '22', '/static/images/ximg.jpg', '222', '0', null, '140', '0', '0', '0', null, '2019-12-17 22:23:30', '2019-12-17 22:23:30');
INSERT INTO `t_article` VALUES ('54', '为什么要学习测试,', '成富婆', '为了搞钱', '/static/images/ximg.jpg', '搞钱是人生大事', '0', null, '64', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('55', 'None', 'None', 'None', '/static/images/ximg.jpg', 'None', '0', null, '72', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('56', '写文章接口', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '72', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('57', '', '', '', '/static/images/ximg.jpg', '', '1', null, '72', '0', '0', '0', null, '2019-12-17 22:10:39', '2019-12-17 22:10:39');
INSERT INTO `t_article` VALUES ('58', '今天要吃烤鸡，烤鸭，烤鱼', '介绍', '嘎嘎嘎，呀呀呀，嘿嘿嘿，呃呃呃', '/static/images/ximg.jpg', '测试', '0', null, '134', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('59', ' ', '介', '内容呀', '/static/images/ximg.jpg', '测试', '0', null, '134', '0', '0', '0', null, '2019-12-18 19:20:20', '2019-12-18 19:20:20');
INSERT INTO `t_article` VALUES ('60', '', '介绍', '内容呀', '/static/images/ximg.jpg', '测试', '0', null, '134', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('61', '测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '134', '0', '0', '0', null, '2019-12-17 23:18:50', '2019-12-17 23:18:50');
INSERT INTO `t_article` VALUES ('62', '晚饭', '烤地瓜吧', '晚饭吃什么呢', '/static/images/ximg.jpg', '美食', '1', null, '151', '0', '1', '0', null, '2019-12-18 19:20:26', '2019-12-18 19:20:26');
INSERT INTO `t_article` VALUES ('63', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '152', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('64', '为什么要学习测试', '介绍', '内容', '/static/images/ximg.jpg', '测试', '0', null, '152', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('65', '', '', '', '/static/images/ximg.jpg', '', '0', null, '152', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('66', '尼', '介绍', '好', '/static/images/ximg.jpg', '呢', '0', null, '152', '0', '0', '0', null, '2019-12-18 19:22:29', '2019-12-18 19:22:29');
INSERT INTO `t_article` VALUES ('68', '为什么要111学习测试', '介绍', '内22111112222容', '/static/images/ximg.jpg', '测试', '0', null, '165', '0', '0', '0', null, null, null);
INSERT INTO `t_article` VALUES ('69', '为什么要111学习测试', '介绍', '内22111112222容', '/static/images/ximg.jpg', '测试', '1', null, '165', '0', '0', '0', null, '2019-12-18 23:52:38', '2019-12-18 23:52:38');

-- ----------------------------
-- Table structure for t_article_user_status
-- ----------------------------
DROP TABLE IF EXISTS `t_article_user_status`;
CREATE TABLE `t_article_user_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `aid` int(11) NOT NULL COMMENT '心得体会文章ID',
  `uid` int(11) NOT NULL COMMENT '用户ID',
  `gstatus` int(11) NOT NULL DEFAULT '1' COMMENT '点赞状态，0点赞，1没点赞',
  `cstatus` int(11) NOT NULL DEFAULT '1' COMMENT '收藏状态，0收藏，1没收藏',
  `fstatus` int(11) NOT NULL DEFAULT '1' COMMENT '关注状态，0关注，1没关注',
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_article_user_status
-- ----------------------------
INSERT INTO `t_article_user_status` VALUES ('1', '1', '23', '1', '0', '1', null);
INSERT INTO `t_article_user_status` VALUES ('2', '1', '25', '1', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('3', '1', '56', '1', '0', '1', null);
INSERT INTO `t_article_user_status` VALUES ('4', '2', '25', '1', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('5', '2', '23', '1', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('6', '15', '23', '1', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('7', '14', '23', '0', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('8', '3', '25', '0', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('9', '5', '25', '0', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('10', '1', '10', '1', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('11', '13', '23', '1', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('12', '22', '23', '1', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('13', '23', '25', '1', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('14', '17', '23', '0', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('15', '22', '56', '0', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('16', '1', '20', '0', '0', '1', null);
INSERT INTO `t_article_user_status` VALUES ('17', '1', '79', '0', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('18', '1', '118', '0', '0', '1', null);
INSERT INTO `t_article_user_status` VALUES ('19', '2', '118', '0', '0', '1', null);
INSERT INTO `t_article_user_status` VALUES ('20', '1', '123', '0', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('21', '1', '81', '1', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('22', '23', '86', '1', '0', '1', null);
INSERT INTO `t_article_user_status` VALUES ('23', '35', '86', '1', '0', '1', null);
INSERT INTO `t_article_user_status` VALUES ('24', '1', '76', '0', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('25', '45', '64', '1', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('26', '1', '141', '0', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('27', '1', '72', '0', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('28', '27', '64', '1', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('29', '12', '25', '1', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('30', '1', '152', '1', '0', '1', null);
INSERT INTO `t_article_user_status` VALUES ('31', '4', '152', '1', '0', '1', null);
INSERT INTO `t_article_user_status` VALUES ('32', '62', '152', '1', '0', '1', null);
INSERT INTO `t_article_user_status` VALUES ('33', '1', '151', '1', '1', '1', null);
INSERT INTO `t_article_user_status` VALUES ('34', '1', '165', '0', '1', '1', null);

-- ----------------------------
-- Table structure for t_coures
-- ----------------------------
DROP TABLE IF EXISTS `t_coures`;
CREATE TABLE `t_coures` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL COMMENT '教程标题',
  `brief` varchar(255) DEFAULT NULL,
  `content` varchar(255) NOT NULL COMMENT '教程内容',
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '状态0正常1删除',
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `ximg` varchar(255) NOT NULL DEFAULT '/static/images/ximg.jpg' COMMENT '显示的图片',
  `tags` varchar(255) DEFAULT NULL COMMENT '分类',
  `remark` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `goods` int(16) DEFAULT '0' COMMENT '点赞数量',
  `collections` int(16) DEFAULT '0' COMMENT '收藏数量',
  `follows` int(16) NOT NULL DEFAULT '0' COMMENT '关注数量',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='教程表';

-- ----------------------------
-- Records of t_coures
-- ----------------------------
INSERT INTO `t_coures` VALUES ('1', '测试基础', null, '1111111111111111111111111111111111111111', '0', '浪晋', '/static/images/ximg.jpg', '测试基础', null, '2019-12-18 19:29:41', '2019-12-18 19:29:41', '4', '0', '0');
INSERT INTO `t_coures` VALUES ('2', '接口测试', null, '我们正学习接口测试', '0', '浪晋', '/static/images/ximg.jpg', '测试基础', null, '2019-12-17 22:32:43', '2019-12-17 22:32:43', '2', '1', '0');
INSERT INTO `t_coures` VALUES ('3', '接口测试', null, '测试测试测试', '0', '林博', '/static/images/ximg.jpg', '测试数', null, '2019-12-16 15:26:03', '2019-12-16 15:26:03', '0', '0', '0');
INSERT INTO `t_coures` VALUES ('4', '接口测试', null, '小hi小hi信号', '0', '啊哈', '/static/images/ximg.jpg', '测试充数的', null, null, null, '0', '0', '0');
INSERT INTO `t_coures` VALUES ('5', '接口测试', null, '好咧', '0', '哦哦', '/static/images/ximg.jpg', '测试吗', null, '2019-12-17 22:28:47', '2019-12-17 22:28:47', '1', '0', '0');
INSERT INTO `t_coures` VALUES ('66', '接口测试', null, '汪昊好像内个金城武啊', '0', '金城武', '/static/images/ximg.jpg', '测试大哥', null, '2019-12-18 19:30:20', '2019-12-18 19:30:20', '2', '0', '0');
INSERT INTO `t_coures` VALUES ('88', '接口测试', null, '汪昊好像内个吴彦祖啊', '0', '吴彦祖', '/static/images/ximg.jpg', '测试大佬', null, '2019-12-17 21:30:01', '2019-12-17 21:30:01', '1', '0', '0');

-- ----------------------------
-- Table structure for t_coures_user_status
-- ----------------------------
DROP TABLE IF EXISTS `t_coures_user_status`;
CREATE TABLE `t_coures_user_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `cid` int(11) NOT NULL COMMENT '教程ID',
  `uid` int(11) NOT NULL COMMENT '用户ID',
  `gstatus` int(11) NOT NULL DEFAULT '1' COMMENT '点赞状态，0点赞，1没点赞',
  `cstatus` int(11) NOT NULL DEFAULT '1' COMMENT '收藏状态，0收藏，1没收藏',
  `fstatus` int(11) NOT NULL DEFAULT '1' COMMENT '关注状态，0关注，1没关注',
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_coures_user_status
-- ----------------------------
INSERT INTO `t_coures_user_status` VALUES ('1', '1', '56', '1', '1', '1', null);
INSERT INTO `t_coures_user_status` VALUES ('2', '2', '23', '0', '1', '1', null);
INSERT INTO `t_coures_user_status` VALUES ('3', '1', '23', '1', '1', '1', null);
INSERT INTO `t_coures_user_status` VALUES ('4', '1', '123', '0', '1', '1', null);
INSERT INTO `t_coures_user_status` VALUES ('5', '1', '76', '0', '1', '1', null);
INSERT INTO `t_coures_user_status` VALUES ('6', '2', '76', '0', '1', '1', null);
INSERT INTO `t_coures_user_status` VALUES ('7', '5', '64', '0', '1', '1', null);
INSERT INTO `t_coures_user_status` VALUES ('8', '1', '141', '0', '1', '1', null);
INSERT INTO `t_coures_user_status` VALUES ('9', '2', '64', '1', '0', '1', null);
INSERT INTO `t_coures_user_status` VALUES ('10', '66', '72', '1', '1', '1', null);
INSERT INTO `t_coures_user_status` VALUES ('11', '66', '25', '1', '1', '1', null);
INSERT INTO `t_coures_user_status` VALUES ('12', '1', '152', '1', '1', '1', null);
INSERT INTO `t_coures_user_status` VALUES ('13', '1', '151', '1', '1', '1', null);
INSERT INTO `t_coures_user_status` VALUES ('14', '66', '141', '0', '1', '1', null);

-- ----------------------------
-- Table structure for t_inspirer
-- ----------------------------
DROP TABLE IF EXISTS `t_inspirer`;
CREATE TABLE `t_inspirer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) NOT NULL,
  `uid` int(11) DEFAULT NULL,
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '状态 0正常 1删除',
  `ximg` varchar(255) NOT NULL DEFAULT '/static/images/ximg.jpg' COMMENT '显示的图片',
  `author` varchar(255) DEFAULT NULL,
  `goods` int(16) DEFAULT '0' COMMENT '点赞数量',
  `collections` int(16) DEFAULT '0' COMMENT '收藏数量',
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8 COMMENT='灵光一闪';

-- ----------------------------
-- Records of t_inspirer
-- ----------------------------
INSERT INTO `t_inspirer` VALUES ('1', '内容', '1', '1', '/static/images/ximg.jpg', null, '1', '1', '2019-12-17 19:41:45', '2019-12-17 19:41:45');
INSERT INTO `t_inspirer` VALUES ('2', '我还是提50个吧', null, '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-17 22:27:59', '2019-12-17 22:27:59');
INSERT INTO `t_inspirer` VALUES ('3', '111', null, '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-17 13:57:34', '2019-12-17 13:57:34');
INSERT INTO `t_inspirer` VALUES ('4', '鄢雨是个苕', null, '0', '/static/images/ximg.jpg', null, '1', '1', '2019-12-18 15:14:45', '2019-12-18 15:14:45');
INSERT INTO `t_inspirer` VALUES ('5', '内容', '56', '0', '/static/images/ximg.jpg', null, '1', '0', '2019-12-18 16:18:13', '2019-12-18 16:18:13');
INSERT INTO `t_inspirer` VALUES ('6', '吃完就睡觉', '56', '0', '/static/images/ximg.jpg', null, '0', '0', '2019-12-18 02:45:43', '2019-12-18 02:45:43');
INSERT INTO `t_inspirer` VALUES ('7', '啥事也不干', '56', '0', '/static/images/ximg.jpg', null, '0', '0', '2019-12-18 02:45:48', '2019-12-18 02:45:48');
INSERT INTO `t_inspirer` VALUES ('8', '加班一小时', '57', '0', '/static/images/ximg.jpg', null, '0', '0', '2019-12-18 15:03:36', '2019-12-18 15:03:36');
INSERT INTO `t_inspirer` VALUES ('9', '还要骂爹娘', '57', '0', '/static/images/ximg.jpg', null, '0', '0', '2019-12-18 02:46:15', '2019-12-18 02:46:15');
INSERT INTO `t_inspirer` VALUES ('10', '!!!!!!', '57', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-18 02:50:39', '2019-12-18 02:50:39');
INSERT INTO `t_inspirer` VALUES ('11', '你好，你是脆皮鸭吗？来重庆好吃街吃酸辣粉撒', '64', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-17 14:17:34', '2019-12-17 14:17:34');
INSERT INTO `t_inspirer` VALUES ('12', '内容', '77', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-17 21:56:12', '2019-12-17 21:56:12');
INSERT INTO `t_inspirer` VALUES ('13', '内容', '83', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('14', '内容', '93', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('15', '黄1', '10', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-18 16:21:43', '2019-12-18 16:21:43');
INSERT INTO `t_inspirer` VALUES ('16', '内容', '10', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('17', '哈哈', '98', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('18', '', '98', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('19', '呵呵', '98', '0', '/static/images/ximg.jpg', null, '1', '0', '2019-12-17 21:45:30', '2019-12-17 21:45:30');
INSERT INTO `t_inspirer` VALUES ('20', '你瞅啥', '98', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-17 22:28:49', '2019-12-17 22:28:49');
INSERT INTO `t_inspirer` VALUES ('21', '瞅你咋地', '98', '0', '/static/images/ximg.jpg', null, '1', '0', '2019-12-17 16:38:15', '2019-12-17 16:38:15');
INSERT INTO `t_inspirer` VALUES ('22', '打不死的小蟑螂是小强', '119', '1', '/static/images/ximg.jpg', null, '1', '0', '2019-12-17 22:02:52', '2019-12-17 22:02:52');
INSERT INTO `t_inspirer` VALUES ('23', '    ', '119', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-17 15:35:07', '2019-12-17 15:35:07');
INSERT INTO `t_inspirer` VALUES ('24', '北京烤鸭超好吃！火锅超好吃！', '64', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('25', '好想吃烤散面啊啊啊，不你不想吃', '64', '0', '/static/images/ximg.jpg', null, '0', '0', '2019-12-18 16:54:30', '2019-12-18 16:54:30');
INSERT INTO `t_inspirer` VALUES ('26', '！', '64', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-17 21:44:33', '2019-12-17 21:44:33');
INSERT INTO `t_inspirer` VALUES ('27', ' ', '64', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-17 21:44:21', '2019-12-17 21:44:21');
INSERT INTO `t_inspirer` VALUES ('28', '', '64', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-17 22:28:17', '2019-12-17 22:28:17');
INSERT INTO `t_inspirer` VALUES ('29', '内容', '79', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('30', '内容1111', '72', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('31', '', '72', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('32', '', '72', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('33', '', '72', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('34', '火锅好吃，来点黄喉，肥肠，藕,虾滑', '64', '0', '/static/images/ximg.jpg', null, '0', '1', '2019-12-17 22:33:07', '2019-12-17 22:33:07');
INSERT INTO `t_inspirer` VALUES ('35', '嘻嘻', '136', '0', '/static/images/ximg.jpg', null, '0', '0', '2019-12-17 22:18:02', '2019-12-17 22:18:02');
INSERT INTO `t_inspirer` VALUES ('36', '人为什么活着', '134', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('37', '111455…………&', '134', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('38', '杨123/-0%', '134', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-18 17:03:31', '2019-12-18 17:03:31');
INSERT INTO `t_inspirer` VALUES ('39', '1111111', '81', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('40', '哈哈哈哈222', '134', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-17 22:32:24', '2019-12-17 22:32:24');
INSERT INTO `t_inspirer` VALUES ('41', '1111111', '81', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('42', '内容', '10', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-17 22:24:29', '2019-12-17 22:24:29');
INSERT INTO `t_inspirer` VALUES ('43', '我还是提50个吧', '10', '0', '/static/images/ximg.jpg', null, '0', '0', '2019-12-17 22:25:43', '2019-12-17 22:25:43');
INSERT INTO `t_inspirer` VALUES ('44', '321', '110', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-17 22:31:27', '2019-12-17 22:31:27');
INSERT INTO `t_inspirer` VALUES ('45', '好想吃烤散面啊啊啊，不你不想吃', '151', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-18 16:59:25', '2019-12-18 16:59:25');
INSERT INTO `t_inspirer` VALUES ('46', '                          ', '164', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('47', '哈哈哈哈哈', '98', '0', '/static/images/ximg.jpg', null, '0', '0', null, null);
INSERT INTO `t_inspirer` VALUES ('48', '内222222容', '165', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-18 23:50:59', '2019-12-18 23:50:59');
INSERT INTO `t_inspirer` VALUES ('49', '内22111112222容', '165', '1', '/static/images/ximg.jpg', null, '0', '0', '2019-12-18 23:50:40', '2019-12-18 23:50:40');

-- ----------------------------
-- Table structure for t_inspirer_user_status
-- ----------------------------
DROP TABLE IF EXISTS `t_inspirer_user_status`;
CREATE TABLE `t_inspirer_user_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `iid` int(11) NOT NULL COMMENT '灵感ID',
  `uid` int(11) NOT NULL COMMENT '用户ID',
  `gstatus` int(255) NOT NULL DEFAULT '1' COMMENT '点赞状态，0点赞，1没点赞',
  `cstatus` int(255) NOT NULL DEFAULT '1' COMMENT '收藏状态，0收藏，1没收藏',
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_inspirer_user_status
-- ----------------------------
INSERT INTO `t_inspirer_user_status` VALUES ('1', '1', '56', '1', '0', null);
INSERT INTO `t_inspirer_user_status` VALUES ('2', '22', '56', '0', '1', null);
INSERT INTO `t_inspirer_user_status` VALUES ('3', '1', '23', '0', '1', null);
INSERT INTO `t_inspirer_user_status` VALUES ('4', '4', '25', '1', '1', null);
INSERT INTO `t_inspirer_user_status` VALUES ('5', '4', '23', '1', '0', null);
INSERT INTO `t_inspirer_user_status` VALUES ('6', '8', '23', '1', '1', null);
INSERT INTO `t_inspirer_user_status` VALUES ('7', '19', '86', '0', '1', null);
INSERT INTO `t_inspirer_user_status` VALUES ('8', '4', '76', '0', '1', null);
INSERT INTO `t_inspirer_user_status` VALUES ('9', '5', '64', '0', '1', null);
INSERT INTO `t_inspirer_user_status` VALUES ('10', '34', '64', '1', '0', null);

-- ----------------------------
-- Table structure for t_questions
-- ----------------------------
DROP TABLE IF EXISTS `t_questions`;
CREATE TABLE `t_questions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL COMMENT '问题题目',
  `brief` varchar(255) DEFAULT NULL COMMENT '简介',
  `content` varchar(255) DEFAULT NULL COMMENT '问题内容',
  `tags` varchar(255) DEFAULT NULL COMMENT '问题分类',
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `goods` int(11) DEFAULT '0' COMMENT '点赞数量',
  `collections` int(11) DEFAULT '0' COMMENT '收藏数量',
  `follows` int(16) NOT NULL DEFAULT '0' COMMENT '关注数量',
  `status` int(11) NOT NULL DEFAULT '0' COMMENT '状态 0正常1删除',
  `ximg` varchar(255) NOT NULL DEFAULT '/static/images/ximg.jpg' COMMENT '显示的图片',
  `uid` int(11) NOT NULL COMMENT '提问人ID',
  `remark` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=257 DEFAULT CHARSET=utf8 COMMENT='交流讨论表';

-- ----------------------------
-- Records of t_questions
-- ----------------------------
INSERT INTO `t_questions` VALUES ('1', 'niubi', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '1', null, '2019-12-17 17:33:51', '2019-12-17 17:33:51');
INSERT INTO `t_questions` VALUES ('2', 'admi....n', null, '123456', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '4', null, '2019-12-17 17:33:51', '2019-12-17 17:33:51');
INSERT INTO `t_questions` VALUES ('3', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '1', null, '2019-12-17 17:33:51', '2019-12-17 17:33:51');
INSERT INTO `t_questions` VALUES ('4', 'admi....n', null, '123456', '测试', null, '0', '1', '0', '0', '/static/images/ximg.jpg', '1', null, '2019-12-18 15:15:31', '2019-12-18 15:15:31');
INSERT INTO `t_questions` VALUES ('5', '为什么要学习测试', '介绍', '内容', '测试', null, '1', '0', '0', '0', '/static/images/ximg.jpg', '1', null, '2019-12-17 22:27:39', '2019-12-17 22:27:39');
INSERT INTO `t_questions` VALUES ('6', '为什么要学习测试', '介绍', '内容', '测试', null, '1', '0', '0', '0', '/static/images/ximg.jpg', '1', null, '2019-12-17 22:10:24', '2019-12-17 22:10:24');
INSERT INTO `t_questions` VALUES ('7', '测试文章标题1', '这是文章的简介', '这是测试文章的内容', '教程', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '21', null, '2019-12-17 17:33:52', '2019-12-17 17:33:52');
INSERT INTO `t_questions` VALUES ('8', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '1', null, '2019-12-17 17:33:52', '2019-12-17 17:33:52');
INSERT INTO `t_questions` VALUES ('9', 'diyi', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '23', null, '2019-12-17 17:33:52', '2019-12-17 17:33:52');
INSERT INTO `t_questions` VALUES ('10', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '1', null, '2019-12-17 17:33:52', '2019-12-17 17:33:52');
INSERT INTO `t_questions` VALUES ('11', 'dier', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '23', null, '2019-12-17 17:33:52', '2019-12-17 17:33:52');
INSERT INTO `t_questions` VALUES ('12', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '20', null, '2019-12-17 17:33:52', '2019-12-17 17:33:52');
INSERT INTO `t_questions` VALUES ('13', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '25', null, '2019-12-17 17:34:04', '2019-12-17 17:34:04');
INSERT INTO `t_questions` VALUES ('14', '11111111111111111111111', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '24', null, '2019-12-17 17:34:04', '2019-12-17 17:34:04');
INSERT INTO `t_questions` VALUES ('15', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '23', null, '2019-12-18 16:59:31', '2019-12-18 16:59:31');
INSERT INTO `t_questions` VALUES ('16', '足球', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '25', null, '2019-12-17 17:34:04', '2019-12-17 17:34:04');
INSERT INTO `t_questions` VALUES ('17', '为什么要学习测试', '介绍', '内容', '测试', null, '1', '1', '0', '0', '/static/images/ximg.jpg', '50', null, '2019-12-17 22:17:40', '2019-12-17 22:17:40');
INSERT INTO `t_questions` VALUES ('18', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '20', null, null, null);
INSERT INTO `t_questions` VALUES ('19', '我来1改', '介1绍', '内1容', '测1试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '6', null, '2019-12-16 16:16:40', '2019-12-16 16:16:40');
INSERT INTO `t_questions` VALUES ('20', 'xu111111', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '6', null, '2019-12-16 16:27:21', '2019-12-16 16:27:21');
INSERT INTO `t_questions` VALUES ('21', 'xu111111', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '6', null, null, null);
INSERT INTO `t_questions` VALUES ('22', '', '介1绍', '内1容', '测1试', null, '1', '0', '0', '0', '/static/images/ximg.jpg', '6', null, '2019-12-17 16:55:19', '2019-12-17 16:55:19');
INSERT INTO `t_questions` VALUES ('24', 'None', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '6', null, '2019-12-18 15:03:28', '2019-12-18 15:03:28');
INSERT INTO `t_questions` VALUES ('25', '', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '6', null, null, null);
INSERT INTO `t_questions` VALUES ('26', '', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '56', null, null, null);
INSERT INTO `t_questions` VALUES ('27', '林博', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '56', null, null, null);
INSERT INTO `t_questions` VALUES ('28', '', '介绍', '林博', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '56', null, null, null);
INSERT INTO `t_questions` VALUES ('29', '阿斯顿发斯蒂芬', '这是一个测试简介！', '<p>阿斯顿发sdfasdf asdf&nbsp;</p><p><br></p>', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '20', null, null, null);
INSERT INTO `t_questions` VALUES ('30', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '57', null, null, null);
INSERT INTO `t_questions` VALUES ('31', '阿斯顿发斯蒂芬', '这是一个测试简介！', '<p>阿斯顿发sdfasdf asdf&nbsp;</p><p><br></p>', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '20', null, null, null);
INSERT INTO `t_questions` VALUES ('32', 'null', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '57', null, null, null);
INSERT INTO `t_questions` VALUES ('33', '', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '57', null, null, null);
INSERT INTO `t_questions` VALUES ('34', '林11博', '介绍', '！！！！', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '56', null, null, null);
INSERT INTO `t_questions` VALUES ('35', '篮球足球', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '57', null, null, null);
INSERT INTO `t_questions` VALUES ('36', '林11博', '介绍', '！！！！', '！！！！！！', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '56', null, null, null);
INSERT INTO `t_questions` VALUES ('37', '林11博', '介绍', '！！！！', '', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '56', null, null, null);
INSERT INTO `t_questions` VALUES ('38', '林11博', '', '！！！！', '', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '56', null, null, null);
INSERT INTO `t_questions` VALUES ('39', '林11博', '', '', '', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '56', null, null, null);
INSERT INTO `t_questions` VALUES ('40', '篮球足球', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '57', null, '2019-12-16 16:42:04', '2019-12-16 16:42:04');
INSERT INTO `t_questions` VALUES ('41', '？？？', '？？', '？？', '？？', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '57', null, '2019-12-16 16:41:28', '2019-12-16 16:41:28');
INSERT INTO `t_questions` VALUES ('42', '', '#', '？', '@', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '57', null, '2019-12-16 17:03:38', '2019-12-16 17:03:38');
INSERT INTO `t_questions` VALUES ('43', '？？？', '？？', '？？', '？？', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '57', null, null, null);
INSERT INTO `t_questions` VALUES ('44', '林11博', '', '', '', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '56', null, null, null);
INSERT INTO `t_questions` VALUES ('45', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '64', null, '2019-12-17 18:54:10', '2019-12-17 18:54:10');
INSERT INTO `t_questions` VALUES ('46', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '64', null, null, null);
INSERT INTO `t_questions` VALUES ('47', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '64', null, '2019-12-17 18:52:16', '2019-12-17 18:52:16');
INSERT INTO `t_questions` VALUES ('48', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('49', 'aaaaaaaaaaa+为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '72', null, '2019-12-17 21:46:35', '2019-12-17 21:46:35');
INSERT INTO `t_questions` VALUES ('50', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '39', null, '2019-12-16 22:59:17', '2019-12-16 22:59:17');
INSERT INTO `t_questions` VALUES ('51', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '39', null, null, null);
INSERT INTO `t_questions` VALUES ('52', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '38', null, null, null);
INSERT INTO `t_questions` VALUES ('53', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('54', 'None', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '76', null, null, null);
INSERT INTO `t_questions` VALUES ('55', '为什么要学习测试', '介绍', '内容', '测试', null, '1', '0', '0', '0', '/static/images/ximg.jpg', '75', null, '2019-12-17 22:34:06', '2019-12-17 22:34:06');
INSERT INTO `t_questions` VALUES ('56', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '76', null, null, null);
INSERT INTO `t_questions` VALUES ('57', '问个问题', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('58', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '1', '0', '0', '/static/images/ximg.jpg', '38', null, '2019-12-17 17:17:32', '2019-12-17 17:17:32');
INSERT INTO `t_questions` VALUES ('59', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '74', null, null, null);
INSERT INTO `t_questions` VALUES ('60', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '80', null, null, null);
INSERT INTO `t_questions` VALUES ('61', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '82', null, null, null);
INSERT INTO `t_questions` VALUES ('62', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '77', null, null, null);
INSERT INTO `t_questions` VALUES ('63', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '51', null, null, null);
INSERT INTO `t_questions` VALUES ('64', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '83', null, null, null);
INSERT INTO `t_questions` VALUES ('65', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '86', null, null, null);
INSERT INTO `t_questions` VALUES ('66', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '1', '0', '0', '/static/images/ximg.jpg', '79', null, '2019-12-18 15:03:58', '2019-12-18 15:03:58');
INSERT INTO `t_questions` VALUES ('67', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '81', null, null, null);
INSERT INTO `t_questions` VALUES ('68', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '88', null, null, null);
INSERT INTO `t_questions` VALUES ('69', 'None', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '90', null, null, null);
INSERT INTO `t_questions` VALUES ('70', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '79', null, null, null);
INSERT INTO `t_questions` VALUES ('71', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '38', null, null, null);
INSERT INTO `t_questions` VALUES ('72', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '92', null, null, null);
INSERT INTO `t_questions` VALUES ('73', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '1', null, null, null);
INSERT INTO `t_questions` VALUES ('74', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '39', null, null, null);
INSERT INTO `t_questions` VALUES ('75', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '80', null, null, null);
INSERT INTO `t_questions` VALUES ('76', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '93', null, null, null);
INSERT INTO `t_questions` VALUES ('77', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '39', null, null, null);
INSERT INTO `t_questions` VALUES ('78', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '39', null, null, null);
INSERT INTO `t_questions` VALUES ('79', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '64', null, '2019-12-17 18:50:57', '2019-12-17 18:50:57');
INSERT INTO `t_questions` VALUES ('80', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '89', null, null, null);
INSERT INTO `t_questions` VALUES ('81', 'None', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '94', null, null, null);
INSERT INTO `t_questions` VALUES ('82', 'None', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '94', null, null, null);
INSERT INTO `t_questions` VALUES ('83', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '80', null, null, null);
INSERT INTO `t_questions` VALUES ('84', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '92', null, null, null);
INSERT INTO `t_questions` VALUES ('85', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '90', null, null, null);
INSERT INTO `t_questions` VALUES ('86', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '92', null, null, null);
INSERT INTO `t_questions` VALUES ('87', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '92', null, null, null);
INSERT INTO `t_questions` VALUES ('88', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '92', null, null, null);
INSERT INTO `t_questions` VALUES ('89', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '92', null, null, null);
INSERT INTO `t_questions` VALUES ('90', '为什么是你', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '76', null, null, null);
INSERT INTO `t_questions` VALUES ('91', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '84', null, null, null);
INSERT INTO `t_questions` VALUES ('92', 'None', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '90', null, null, null);
INSERT INTO `t_questions` VALUES ('93', '为什么是你', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '76', null, null, null);
INSERT INTO `t_questions` VALUES ('94', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '98', null, null, null);
INSERT INTO `t_questions` VALUES ('95', '为什么是你', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '76', null, null, null);
INSERT INTO `t_questions` VALUES ('96', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '98', null, null, null);
INSERT INTO `t_questions` VALUES ('97', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '98', null, null, null);
INSERT INTO `t_questions` VALUES ('98', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '99', null, null, null);
INSERT INTO `t_questions` VALUES ('99', ' ', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('100', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '98', null, null, null);
INSERT INTO `t_questions` VALUES ('101', '11111', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('102', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '98', null, null, null);
INSERT INTO `t_questions` VALUES ('103', '为什么学习测试呢', '介绍1', '内容123', '测试12', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '97', null, null, null);
INSERT INTO `t_questions` VALUES ('104', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '101', null, null, null);
INSERT INTO `t_questions` VALUES ('105', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('106', 'None', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '100', null, null, null);
INSERT INTO `t_questions` VALUES ('107', ' ', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '97', null, null, null);
INSERT INTO `t_questions` VALUES ('108', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '100', null, null, null);
INSERT INTO `t_questions` VALUES ('109', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '100', null, null, null);
INSERT INTO `t_questions` VALUES ('110', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '98', null, null, null);
INSERT INTO `t_questions` VALUES ('111', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '100', null, null, null);
INSERT INTO `t_questions` VALUES ('112', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('113', '1为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('114', '为什么要学习', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '100', null, null, null);
INSERT INTO `t_questions` VALUES ('115', '1为什么要学AAAAAAAA习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('116', '为什么要学习测试呢 ', '介绍', '内容测试', ' ', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '97', null, null, null);
INSERT INTO `t_questions` VALUES ('117', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '98', null, null, null);
INSERT INTO `t_questions` VALUES ('118', '为什么要学习测试呢 ', '简介呀', '内容测试', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '97', null, null, null);
INSERT INTO `t_questions` VALUES ('119', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('120', '为什么要学11111习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('121', '为什么要学11111习测试', '介11绍', '11内容', '测11试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('122', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '100', null, null, null);
INSERT INTO `t_questions` VALUES ('123', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('124', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '100', null, null, null);
INSERT INTO `t_questions` VALUES ('125', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '99', null, null, null);
INSERT INTO `t_questions` VALUES ('126', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '99', null, null, null);
INSERT INTO `t_questions` VALUES ('127', '我为啥这么帅嘞', '介绍', '天生的，没办法', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '98', null, '2019-12-17 14:06:32', '2019-12-17 14:06:32');
INSERT INTO `t_questions` VALUES ('128', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '10', null, null, null);
INSERT INTO `t_questions` VALUES ('129', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '99', null, null, null);
INSERT INTO `t_questions` VALUES ('130', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '112', null, null, null);
INSERT INTO `t_questions` VALUES ('131', '容嬷嬷', '介绍', '紫薇', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '76', null, '2019-12-17 11:10:41', '2019-12-17 11:10:41');
INSERT INTO `t_questions` VALUES ('132', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '117', null, null, null);
INSERT INTO `t_questions` VALUES ('133', '为什么要学习开发', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '98', null, '2019-12-17 13:59:57', '2019-12-17 13:59:57');
INSERT INTO `t_questions` VALUES ('134', '为什么', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '98', null, null, null);
INSERT INTO `t_questions` VALUES ('135', '为什么', '介绍', '1', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '98', null, null, null);
INSERT INTO `t_questions` VALUES ('136', '为什么', '介绍', '1', '2', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '98', null, null, null);
INSERT INTO `t_questions` VALUES ('137', '为什么', '3', '1', '2', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '98', null, null, null);
INSERT INTO `t_questions` VALUES ('138', '1', '3', '1', '2', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '98', null, null, null);
INSERT INTO `t_questions` VALUES ('139', '', '', '', '', null, '1', '0', '0', '0', '/static/images/ximg.jpg', '98', null, '2019-12-17 16:58:54', '2019-12-17 16:58:54');
INSERT INTO `t_questions` VALUES ('140', '为啥', '哈哈', '不知道', '呵呵', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '98', null, null, null);
INSERT INTO `t_questions` VALUES ('141', '为什么要吃饭', '民以食为天', '人是铁饭是钢', '民间疾苦', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '119', null, '2019-12-17 15:14:21', '2019-12-17 15:14:21');
INSERT INTO `t_questions` VALUES ('142', '为什么要吃饭', '民以食为天', '人是铁饭是钢', '民间疾苦', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '119', null, null, null);
INSERT INTO `t_questions` VALUES ('143', '为什么要吃饭', '民以食为天', '人是铁饭是钢', '民间疾苦', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '119', null, null, null);
INSERT INTO `t_questions` VALUES ('144', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '118', null, null, null);
INSERT INTO `t_questions` VALUES ('145', '', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '118', null, null, null);
INSERT INTO `t_questions` VALUES ('146', '为什么要学习测试', '介绍', '', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '118', null, null, null);
INSERT INTO `t_questions` VALUES ('147', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '118', null, null, null);
INSERT INTO `t_questions` VALUES ('148', '为什么要学习测试', '介绍', '看看', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '118', null, null, null);
INSERT INTO `t_questions` VALUES ('149', '就要学习测试', '介绍', '看看', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '118', null, null, null);
INSERT INTO `t_questions` VALUES ('150', '阿斯顿发斯蒂芬', '这是一个测试简介！', '<p>阿斯顿发sdfasdf asdf&nbsp;</p><p><br></p>', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '20', null, null, null);
INSERT INTO `t_questions` VALUES ('151', '', '介绍', '看看', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '118', null, null, null);
INSERT INTO `t_questions` VALUES ('152', '', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '10', null, null, null);
INSERT INTO `t_questions` VALUES ('153', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '121', null, null, null);
INSERT INTO `t_questions` VALUES ('154', '阿斯顿发送到发多少f', '这是一个测试简介！', '<p>阿斯顿发阿斯顿发阿斯顿发</p>', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '39', null, null, null);
INSERT INTO `t_questions` VALUES ('155', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '10', null, null, null);
INSERT INTO `t_questions` VALUES ('156', '测试大法好', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '64', null, '2019-12-17 18:50:20', '2019-12-17 18:50:20');
INSERT INTO `t_questions` VALUES ('157', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '64', null, '2019-12-17 18:50:46', '2019-12-17 18:50:46');
INSERT INTO `t_questions` VALUES ('158', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '64', null, '2019-12-17 18:50:51', '2019-12-17 18:50:51');
INSERT INTO `t_questions` VALUES ('159', '阿斯顿发斯蒂芬', '这是一个测试简介！', '<p>阿斯顿发sdfasdf asdf&nbsp;</p><p><br></p>', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '20', null, null, null);
INSERT INTO `t_questions` VALUES ('160', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '105', null, null, null);
INSERT INTO `t_questions` VALUES ('161', '第一次测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '105', null, null, null);
INSERT INTO `t_questions` VALUES ('162', '为什么要学习测试1', '介绍1', '内容1', '测试1', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '123', null, null, null);
INSERT INTO `t_questions` VALUES ('163', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '105', null, null, null);
INSERT INTO `t_questions` VALUES ('164', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '123', null, null, null);
INSERT INTO `t_questions` VALUES ('165', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '10', null, '2019-12-17 18:49:21', '2019-12-17 18:49:21');
INSERT INTO `t_questions` VALUES ('166', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '79', null, null, null);
INSERT INTO `t_questions` VALUES ('167', '烟雨为什么这么聪明', '介绍', '没有为什么', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '10', null, null, null);
INSERT INTO `t_questions` VALUES ('168', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('169', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('170', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('171', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('172', '为什1么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('173', '', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('174', '', '介绍', '', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('175', '', '', '', '', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '72', null, '2019-12-17 21:47:27', '2019-12-17 21:47:27');
INSERT INTO `t_questions` VALUES ('176', '', '', '', '', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '72', null, '2019-12-17 21:47:10', '2019-12-17 21:47:10');
INSERT INTO `t_questions` VALUES ('177', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '112', null, null, null);
INSERT INTO `t_questions` VALUES ('178', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '93', null, null, null);
INSERT INTO `t_questions` VALUES ('179', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '131', null, null, null);
INSERT INTO `t_questions` VALUES ('180', 'None', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('181', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('182', '小柱', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '72', null, null, null);
INSERT INTO `t_questions` VALUES ('183', '为什么要学习测试w', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '131', null, '2019-12-17 21:48:00', '2019-12-17 21:48:00');
INSERT INTO `t_questions` VALUES ('184', 'None', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '81', null, null, null);
INSERT INTO `t_questions` VALUES ('185', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '81', null, null, null);
INSERT INTO `t_questions` VALUES ('186', 'None', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '136', null, null, null);
INSERT INTO `t_questions` VALUES ('187', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '136', null, null, null);
INSERT INTO `t_questions` VALUES ('188', '林淯修改', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '133', null, '2019-12-17 21:49:56', '2019-12-17 21:49:56');
INSERT INTO `t_questions` VALUES ('189', '林淯修改', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '133', null, '2019-12-17 21:50:01', '2019-12-17 21:50:01');
INSERT INTO `t_questions` VALUES ('190', '为什么要学习测试 ', '简介呀', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '134', null, null, null);
INSERT INTO `t_questions` VALUES ('191', '', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '77', null, null, null);
INSERT INTO `t_questions` VALUES ('192', '为什么要学学习测试 ', '简介呀', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '134', null, null, null);
INSERT INTO `t_questions` VALUES ('193', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '136', null, null, null);
INSERT INTO `t_questions` VALUES ('194', '', '介绍', '内容', '', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '77', null, null, null);
INSERT INTO `t_questions` VALUES ('195', '', '', '内容', '', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '77', null, null, null);
INSERT INTO `t_questions` VALUES ('196', '', '', '', '', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '77', null, null, null);
INSERT INTO `t_questions` VALUES ('197', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '136', null, null, null);
INSERT INTO `t_questions` VALUES ('198', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '136', null, null, null);
INSERT INTO `t_questions` VALUES ('199', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '123', null, null, null);
INSERT INTO `t_questions` VALUES ('200', '阿拉斯加', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '134', null, '2019-12-17 22:06:00', '2019-12-17 22:06:00');
INSERT INTO `t_questions` VALUES ('201', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '136', null, null, null);
INSERT INTO `t_questions` VALUES ('202', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '82', null, null, null);
INSERT INTO `t_questions` VALUES ('203', '测试删除', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '82', null, '2019-12-17 21:55:20', '2019-12-17 21:55:20');
INSERT INTO `t_questions` VALUES ('204', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '81', null, null, null);
INSERT INTO `t_questions` VALUES ('205', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '136', null, null, null);
INSERT INTO `t_questions` VALUES ('206', '2223', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '82', null, '2019-12-17 21:58:18', '2019-12-17 21:58:18');
INSERT INTO `t_questions` VALUES ('207', '吃饭了吗', '', '今天天气不错', '要不我请你吃饭', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '136', null, '2019-12-17 22:17:04', '2019-12-17 22:17:04');
INSERT INTO `t_questions` VALUES ('208', '测试123', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '81', null, '2019-12-17 22:08:26', '2019-12-17 22:08:26');
INSERT INTO `t_questions` VALUES ('209', '好好学习，天天向上', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '112', null, null, null);
INSERT INTO `t_questions` VALUES ('210', '你从哪里来，我的姑娘', '我去找你', '火星', '哦哦', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '79', null, null, null);
INSERT INTO `t_questions` VALUES ('211', '你从哪里来，我的姑娘', '我去找你', '火星', '哦哦', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '79', null, null, null);
INSERT INTO `t_questions` VALUES ('212', '要学习测试吗11', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '79', null, null, null);
INSERT INTO `t_questions` VALUES ('213', '毛主席说', '介绍啥？', '没有内容', '测试得好好测', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '112', null, '2019-12-18 23:54:08', '2019-12-18 23:54:08');
INSERT INTO `t_questions` VALUES ('214', '为什么要学习测试', '介绍', '内容', '测试', null, '1', '0', '0', '0', '/static/images/ximg.jpg', '133', null, '2019-12-17 22:33:56', '2019-12-17 22:33:56');
INSERT INTO `t_questions` VALUES ('215', 'linxyuin', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '133', null, '2019-12-17 22:26:08', '2019-12-17 22:26:08');
INSERT INTO `t_questions` VALUES ('216', 'linxyuin', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '133', null, null, null);
INSERT INTO `t_questions` VALUES ('217', 'None', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '142', null, null, null);
INSERT INTO `t_questions` VALUES ('218', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '142', null, null, null);
INSERT INTO `t_questions` VALUES ('219', '', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '142', null, null, null);
INSERT INTO `t_questions` VALUES ('220', 'null', 'null', 'null', 'null', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '142', null, null, null);
INSERT INTO `t_questions` VALUES ('221', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '147', null, null, null);
INSERT INTO `t_questions` VALUES ('222', '1', '这是一个测试简介！', '<p>1</p>', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '39', null, null, null);
INSERT INTO `t_questions` VALUES ('223', '1', '这是一个测试简介！', '<p>1</p>', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '39', null, null, null);
INSERT INTO `t_questions` VALUES ('224', '1', '这是一个测试简介！', '<p>1</p>', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '39', null, null, null);
INSERT INTO `t_questions` VALUES ('225', '1', '这是一个测试简介！', '<p>1</p>', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '39', null, null, null);
INSERT INTO `t_questions` VALUES ('226', '1', '这是一个测试简介！', '<p>1</p>', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '39', null, null, null);
INSERT INTO `t_questions` VALUES ('227', '1', '这是一个测试简介！', '<p>1</p>', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '39', null, null, null);
INSERT INTO `t_questions` VALUES ('228', 'None', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '151', null, null, null);
INSERT INTO `t_questions` VALUES ('229', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '151', null, null, null);
INSERT INTO `t_questions` VALUES ('230', 'None', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '151', null, null, null);
INSERT INTO `t_questions` VALUES ('231', 'None', 'None', 'None', 'None', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '151', null, null, null);
INSERT INTO `t_questions` VALUES ('232', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '151', null, null, null);
INSERT INTO `t_questions` VALUES ('233', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '151', null, null, null);
INSERT INTO `t_questions` VALUES ('234', '憨憨为什么要学习测试', '介绍', '因为你憨憨', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '151', null, '2019-12-18 16:48:15', '2019-12-18 16:48:15');
INSERT INTO `t_questions` VALUES ('235', '1', '这是一个测试简介！', '<p>1</p>', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '39', null, null, null);
INSERT INTO `t_questions` VALUES ('236', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '152', null, null, null);
INSERT INTO `t_questions` VALUES ('237', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '152', null, null, null);
INSERT INTO `t_questions` VALUES ('238', '1', '这是一个测试简介！', '<p>1&nbsp;&nbsp;&nbsp;&nbsp;</p>', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '39', null, null, null);
INSERT INTO `t_questions` VALUES ('239', '1111111111', '111111', '<p>111</p>', '111', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '20', null, null, null);
INSERT INTO `t_questions` VALUES ('240', '1', '1', '<p>1<br></p>', '1', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '21', null, null, null);
INSERT INTO `t_questions` VALUES ('241', '1', '1', '<p>1</p>', '1', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '21', null, null, null);
INSERT INTO `t_questions` VALUES ('242', '1', '1', '<p>&nbsp;&nbsp;&nbsp; 1<br></p>', '1', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '21', null, null, null);
INSERT INTO `t_questions` VALUES ('243', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '99', null, null, null);
INSERT INTO `t_questions` VALUES ('244', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '99', null, '2019-12-18 18:29:12', '2019-12-18 18:29:12');
INSERT INTO `t_questions` VALUES ('245', '汪昊为什么可以这么帅', '又勤奋', '一直都很帅', '人又聪明', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '99', null, null, null);
INSERT INTO `t_questions` VALUES ('246', '汪昊为什么可以这么帅', '(｡･㉨･｡)ﾉ♡ ', '๑乛◡乛๑ ', 'ε=(･д･｀*)ﾊｧ', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '99', null, '2019-12-18 19:43:51', '2019-12-18 19:43:51');
INSERT INTO `t_questions` VALUES ('247', '汪昊为什么可以这么帅', '๑乛◡乛๑', '一直都很帅', '(｡･㉨･｡)ﾉ♡ ', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '99', null, null, null);
INSERT INTO `t_questions` VALUES ('248', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '99', null, null, null);
INSERT INTO `t_questions` VALUES ('249', '为什么要学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '152', null, null, null);
INSERT INTO `t_questions` VALUES ('250', '清晨起来拥抱太阳', '介绍', '恩恩', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '155', null, '2019-12-18 23:53:33', '2019-12-18 23:53:33');
INSERT INTO `t_questions` VALUES ('251', '1', '1', '<p>1</p>', '1', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '21', null, null, null);
INSERT INTO `t_questions` VALUES ('252', '为什么要学习测试234', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '155', null, null, null);
INSERT INTO `t_questions` VALUES ('253', '测试234', '介绍', 'haode', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '155', null, null, null);
INSERT INTO `t_questions` VALUES ('254', '修改的内容', '介绍', '内容', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '155', null, '2019-12-18 23:10:27', '2019-12-18 23:10:27');
INSERT INTO `t_questions` VALUES ('255', 'haoluo', '介绍', '恩恩', '测试', null, '0', '0', '0', '0', '/static/images/ximg.jpg', '155', null, null, null);
INSERT INTO `t_questions` VALUES ('256', '为什么要111学习测试', '介绍', '内容', '测试', null, '0', '0', '0', '1', '/static/images/ximg.jpg', '165', null, '2019-12-18 23:43:05', '2019-12-18 23:43:05');

-- ----------------------------
-- Table structure for t_questions_user_status
-- ----------------------------
DROP TABLE IF EXISTS `t_questions_user_status`;
CREATE TABLE `t_questions_user_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `qid` int(11) NOT NULL COMMENT '问题ID',
  `uid` int(11) NOT NULL COMMENT '用户ID',
  `gstatus` int(11) NOT NULL DEFAULT '1' COMMENT '点赞状态，0点赞，1没点赞',
  `cstatus` int(11) NOT NULL DEFAULT '1' COMMENT '收藏状态，0收藏，1没收藏',
  `fstatus` int(11) NOT NULL DEFAULT '1' COMMENT '关注状态，0关注，1没关注',
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_questions_user_status
-- ----------------------------
INSERT INTO `t_questions_user_status` VALUES ('1', '17', '23', '0', '1', '1', null);
INSERT INTO `t_questions_user_status` VALUES ('2', '22', '56', '0', '1', '1', null);
INSERT INTO `t_questions_user_status` VALUES ('3', '5', '25', '0', '1', '1', null);
INSERT INTO `t_questions_user_status` VALUES ('4', '139', '23', '0', '1', '1', null);
INSERT INTO `t_questions_user_status` VALUES ('5', '5', '56', '1', '0', '1', null);
INSERT INTO `t_questions_user_status` VALUES ('6', '17', '25', '1', '0', '1', null);
INSERT INTO `t_questions_user_status` VALUES ('7', '58', '23', '1', '1', '1', null);
INSERT INTO `t_questions_user_status` VALUES ('8', '58', '56', '1', '0', '1', null);
INSERT INTO `t_questions_user_status` VALUES ('9', '6', '76', '0', '1', '1', null);
INSERT INTO `t_questions_user_status` VALUES ('10', '17', '76', '1', '1', '1', null);
INSERT INTO `t_questions_user_status` VALUES ('11', '5', '64', '0', '1', '1', null);
INSERT INTO `t_questions_user_status` VALUES ('12', '214', '133', '0', '1', '1', null);
INSERT INTO `t_questions_user_status` VALUES ('13', '55', '133', '0', '1', '1', null);
INSERT INTO `t_questions_user_status` VALUES ('14', '24', '25', '1', '1', '1', null);
INSERT INTO `t_questions_user_status` VALUES ('15', '66', '25', '1', '0', '1', null);
INSERT INTO `t_questions_user_status` VALUES ('16', '4', '25', '1', '0', '1', null);

-- ----------------------------
-- Table structure for t_title_img
-- ----------------------------
DROP TABLE IF EXISTS `t_title_img`;
CREATE TABLE `t_title_img` (
  `id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL COMMENT '轮播图标题',
  `content` varchar(255) DEFAULT NULL COMMENT '轮播图内容',
  `imghost` varchar(255) NOT NULL,
  `rurl` varchar(255) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='轮播图表';

-- ----------------------------
-- Records of t_title_img
-- ----------------------------
INSERT INTO `t_title_img` VALUES ('1', '不积跬步无以至千里', '人啊就是要努力', '/static/images/1.jpg', null, null, '2019-12-16 15:23:12', '2019-12-16 15:23:12');
INSERT INTO `t_title_img` VALUES ('2', '今天不学习明天吃不上饭', '不学习的人生是没有意义的', '/static/images/1.jpg', null, null, '2019-12-16 15:23:14', '2019-12-16 15:23:14');
INSERT INTO `t_title_img` VALUES ('3', '大吉大利', '今晚吃鸡', '/static/images/1.jpg', null, null, '2019-12-16 15:23:19', '2019-12-16 15:23:19');

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
) ENGINE=InnoDB AUTO_INCREMENT=166 DEFAULT CHARSET=utf8 COMMENT='用户表';

-- ----------------------------
-- Records of t_user
-- ----------------------------
INSERT INTO `t_user` VALUES ('1', 'admin', '123456', 'b8ddd1442485fba8eb0b0a18a5fe539f9ffb26b6', null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('2', 'admi...n', '123456', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('3', 'admi.....n', '123456', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('4', 'admi....n', '123456', '5862c4550896b0090f54e309c8822df279a7f5da', null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('5', 'yujing', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('6', '123456', '123456789', null, '我被修改了', '', '', '123', '', '', '', '', '', '', '', '0', null, '2019-12-17 14:30:53', '2019-12-17 14:30:53');
INSERT INTO `t_user` VALUES ('7', '123456789', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('8', '1234567', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('9', '12345678', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('10', 'yujing123456', '12345678', null, '烟雨', '', '', '@@@@@@@', '@', '@@@', '@@@', '', '', '', '', '0', null, '2019-12-17 16:13:11', '2019-12-17 16:13:11');
INSERT INTO `t_user` VALUES ('11', 'yujing1234', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('12', 'yujing123', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('13', '123121212', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('15', '123456788', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('16', '12345898', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('17', 'yujing123123', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('18', 'iiii23yi', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('19', '0000000', '00000000', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('20', 'admin1234', '123451116', 'b17be390cc56bfa0d9a305a3575e212f3968bfb5', null, null, null, null, null, null, null, null, null, null, null, '0', null, '2019-12-11 16:08:16', '2019-12-11 16:08:16');
INSERT INTO `t_user` VALUES ('21', '1', '1', '3f711160a28c850c787fba5635ec3a1152cb951d', '123', null, null, null, null, null, null, null, null, null, null, '0', null, '2019-12-13 14:27:49', '2019-12-13 14:27:49');
INSERT INTO `t_user` VALUES ('22', 'yujing1233', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('23', 'xutest', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('24', '111111111', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('25', 'yushui', '12312312', null, '张三', '//', '//', '123', '男', '测试', 'hhh@163.com', '79873', 'bdc d', '啊哈哈哈', '成都', '0', null, '2019-12-13 15:11:04', '2019-12-13 15:11:04');
INSERT INTO `t_user` VALUES ('30', 'wangwu', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('31', 'dagege', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('32', 'llllll', '888888888', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('33', 'llllll1', '888888888', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('34', 'llllll14', '888888888', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('35', 'llllll14111', '888888888', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('36', 'llllll141112', '888888888', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('37', 'yanyu2222', '888888888', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('38', 'qwe12345', '1111111111', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('39', 'test123', '123123123', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('40', 'test111', '123123123', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('41', 'test222', '123123123', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('42', '123123123', 'aaaaaaddd', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('43', '12312312312', '31231231231a', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('44', 'yubo1', '23123123123a', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, '2019-12-16 15:55:07', '2019-12-16 15:55:07');
INSERT INTO `t_user` VALUES ('45', '123123', '123123123as', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('46', '12312312', 'asdfasdf ', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('47', 'gxm123456', 'gu786808986u', null, '林博', null, null, null, null, null, null, null, null, null, null, '0', null, '2019-12-16 15:12:30', '2019-12-16 15:12:30');
INSERT INTO `t_user` VALUES ('48', '2mi1234', '123edrhn', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('49', 'zhuce1216', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('50', 'gxmm123456', 'gxm12346', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('51', 'aaaaa6', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('52', 'aaaaa7', '123   45', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('53', 'aaaaa67', '123   ,,45', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('55', 'linbo123', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('56', '1367495611', '1234567890', null, '', '', '', '', '', '', '', '', '', '', '', '0', null, '2019-12-17 14:26:12', '2019-12-17 14:26:12');
INSERT INTO `t_user` VALUES ('57', 'yuanquan', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('58', '136131', '1234567890111', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('59', '1361131', '1234567890111111', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('60', 'yuanquan1', '1234567812345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('61', 'yuanquan2', '123456781', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('62', 'yuanquan3', '1234567811', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('63', '111111', '1234567811', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('64', 'jing123', 'jing123456', null, 'jing12', '', '', '13594167580', '11111', '', '', '', '', '', '', '0', null, '2019-12-17 17:07:57', '2019-12-17 17:07:57');
INSERT INTO `t_user` VALUES ('65', 'jing1234', 'jing123456', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('66', '123456123456', 'jing123456', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('67', 'a1234567', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('68', 'a123459', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('69', 'a12345919', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('70', 'a123459123', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('71', 'a12789105', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('72', 'xzz2017', 'bb19931213', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('73', 'guo2222', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('74', '1212121', 'a12121212', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('75', '123435aaa', 'Aa123213', null, 'Lin', '', '', '欧文i区分我#@i', '哈#@哈', '大撒大撒@@#', '哇哇@#哇', '嘿#@嘿嘿嘿', 'i嘻嘻@#嘻', '', '', '0', null, '2019-12-16 21:37:35', '2019-12-16 21:37:35');
INSERT INTO `t_user` VALUES ('76', 'gxm12345678', 'gxm12345678', null, '南瓜', '土豆', '123', '123', '123', '四季豆', '123', '辣椒', 'gx', '绿豆', '123', '0', null, '2019-12-17 12:49:09', '2019-12-17 12:49:09');
INSERT INTO `t_user` VALUES ('77', 'right7', '12345678', null, '左右', '', '', '', '男', '', '', '', '', '', '', '0', null, '2019-12-16 20:44:33', '2019-12-16 20:44:33');
INSERT INTO `t_user` VALUES ('78', '456789', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('79', 'aa2347', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('80', '98562as', '789412365', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('81', 'zcczcc', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('82', 'xuyannan', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('83', '12341234', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('84', 'aaaaaaaa', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('85', 'haha986', 'Abc98654321', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('86', 'yangyang', '12345678', null, '迪斯尼', '', '', '', '', '', '', '', '', '', '', '0', null, '2019-12-17 16:30:09', '2019-12-17 16:30:09');
INSERT INTO `t_user` VALUES ('87', 'huangmei', '1111111111', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('88', 'abc123456', 'abc123456', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('89', '666666', '88998899', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('90', 'bx905627', '2026905qq', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('91', '11111y', 'yangshaona123', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('92', '321321321', 'a321321321', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('93', 'z12345678', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('94', '123111123123', '1241241241', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('95', '1111222', '12311333', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('96', '11121y', 'yangshaona123', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('97', 'y11121', 'yangshaona123', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('98', 'a123123123', 'a123123123', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('99', 'wanghao123', 'a11111111', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('100', 'yangyang123', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('101', 'bxg905627', '20269052020', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('102', 'aaaaaa', 'aaaaaaaa', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('103', '222aaa', '~!@#$%^&*', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('104', '1234568', '2221542634', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('105', 'lzk123', 'lzk123..', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('106', '333333333', 'aaaaaaaa', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('107', '111aaaaa', '~!@#$%^&*', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('108', '1111aaaa', '_aaaaaa a2222222', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('109', '11a1aaaa', '_aaaaaaa2222222', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('110', 'aaaa33', '_aaaaaa a2222222', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('111', 'aaaaaaaaaaaa', '_aaaaaa a2222222', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('112', 'yang1234', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('113', 'qw345646', 'gu786808986u', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('114', '12sd89uy', '123hn/12', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('115', '123sd89uy', '123hnGGGG', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('116', '112233', 'wwq123456', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('117', 'a112233', 'wwq123456', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('118', 'aaaaaaaa9', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('119', 'yangqinglong', '1234567asd', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('120', '22233444', '12      34', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('121', 'yiyiyiyi', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('122', 'laurence', 'yy123456', null, '瞎眼大侠', ' ', ' ', '  ', ' ', ' ', '  ', '  ', '  ', '  ', '  ', '0', null, '2019-12-17 16:25:48', '2019-12-17 16:25:48');
INSERT INTO `t_user` VALUES ('123', 'y12345', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('124', 'yyyy1234', '222 1542634', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('125', '66661166', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('126', '666668', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('127', '625252525256', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('128', '1526354852', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('129', '15263524852', '12358859', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('130', '152635224852', '1225256845358859', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('131', 'px12345', '22222222', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('132', 'huanghuang', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('133', 'linyuxin', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('134', 'y19980430', 'yangshaona123', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('135', 'right7777777', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('136', 'z1234567', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('137', 'left7777777', '1234678901234~!@', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('138', '111222', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('139', '11122266666', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('140', '1111111', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('141', '1112222', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('142', 'chengguoguo', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('143', '111114', '111111111', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('144', '123456789012', '111111111', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('145', '12345678901', '111111111', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('146', '12345672', '￥￥￥￥￥￥￥￥', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('147', 'chihuoguo', 'chirou123', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('148', '1jing123', 'jing123456789012', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('149', '123arrs', '1234.567', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('150', '123karrs', '12 3 4.567', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('151', 'zxcvbnm', '123456789', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('152', '123456787890', 'ww1jkl2345', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('153', 'wanghao233', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('154', 'admin1224', '11111111', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('155', 'a135792468', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('156', 'abc123', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('157', 'abcde123', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('158', '11fdfffdss11', '11fffffffffff111', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('159', '12345', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('160', '123456ab', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('161', '123456abed59', '12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('162', '12345vvbed59', '!12345678', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('163', '12345vvbeh59', '!12345678&', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('164', '12345vvbel59', '!123456&', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
INSERT INTO `t_user` VALUES ('165', '11fdffdss11', '11fffffffffff111', null, null, null, null, null, null, null, null, null, null, null, null, '0', null, null, null);
