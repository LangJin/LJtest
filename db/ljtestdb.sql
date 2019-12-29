/*
Navicat MySQL Data Transfer

Source Server         : 浪晋的腾讯云
Source Server Version : 50726
Source Host           : 192.144.148.91:3306
Source Database       : ljtestdb

Target Server Type    : MYSQL
Target Server Version : 50726
File Encoding         : 65001

Date: 2019-12-30 02:36:34
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_admin
-- ----------------------------
DROP TABLE IF EXISTS `t_admin`;
CREATE TABLE `t_admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL COMMENT '账号',
  `password` varchar(255) NOT NULL COMMENT '密码',
  `token` varchar(255) DEFAULT NULL COMMENT 'token',
  `nickname` varchar(255) DEFAULT NULL,
  `headpic` varchar(255) DEFAULT 'headimg.jpg' COMMENT '头像',
  `phone` varchar(255) DEFAULT NULL,
  `sex` varchar(255) DEFAULT NULL,
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '0正常1删除2拉黑',
  `remark` varchar(255) DEFAULT NULL COMMENT '昵称',
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='用户表';

-- ----------------------------
-- Table structure for t_article
-- ----------------------------
DROP TABLE IF EXISTS `t_article`;
CREATE TABLE `t_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL COMMENT '题目',
  `brief` varchar(255) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL COMMENT '内容',
  `ximg` varchar(255) NOT NULL DEFAULT 'ximg.jpg' COMMENT '图片显示',
  `tags` varchar(255) DEFAULT NULL COMMENT '分类',
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '状态，0正常1删除',
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `uid` int(11) DEFAULT NULL COMMENT '用户id',
  `goods` int(16) NOT NULL DEFAULT '0' COMMENT '点赞数量',
  `collections` int(16) NOT NULL DEFAULT '0' COMMENT '收藏数量',
  `follows` int(16) NOT NULL DEFAULT '0' COMMENT '关注数量',
  `remark` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='心得体会';

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
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_coures
-- ----------------------------
DROP TABLE IF EXISTS `t_coures`;
CREATE TABLE `t_coures` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `title` varchar(255) NOT NULL COMMENT '教程标题',
  `brief` varchar(255) DEFAULT NULL,
  `content` varchar(255) NOT NULL COMMENT '教程内容',
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '状态0正常1删除',
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `ximg` varchar(255) NOT NULL DEFAULT 'ximg.jpg' COMMENT '显示的图片',
  `tags` varchar(255) DEFAULT NULL COMMENT '分类',
  `remark` varchar(255) DEFAULT NULL,
  `goods` int(16) DEFAULT '0' COMMENT '点赞数量',
  `collections` int(16) DEFAULT '0' COMMENT '收藏数量',
  `follows` int(16) NOT NULL DEFAULT '0' COMMENT '关注数量',
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='教程表';

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
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_inspirer
-- ----------------------------
DROP TABLE IF EXISTS `t_inspirer`;
CREATE TABLE `t_inspirer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) NOT NULL,
  `uid` int(11) DEFAULT NULL,
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '状态 0正常 1删除',
  `ximg` varchar(255) NOT NULL DEFAULT 'ximg.jpg' COMMENT '显示的图片',
  `author` varchar(255) DEFAULT NULL,
  `goods` int(16) DEFAULT '0' COMMENT '点赞数量',
  `collections` int(16) DEFAULT '0' COMMENT '收藏数量',
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='灵光一闪';

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
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

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
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='交流讨论表';

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
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_title_img
-- ----------------------------
DROP TABLE IF EXISTS `t_title_img`;
CREATE TABLE `t_title_img` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL COMMENT '轮播图标题',
  `content` varchar(255) DEFAULT NULL COMMENT '轮播图内容',
  `imghost` varchar(255) NOT NULL,
  `rurl` varchar(255) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='轮播图表';

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
  `titlepic` varchar(255) DEFAULT 'titleimg.jpg',
  `headpic` varchar(255) DEFAULT 'headimg.jpg' COMMENT '头像',
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
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10000 DEFAULT CHARSET=utf8 COMMENT='用户表';

-- ----------------------------
-- Table structure for t_user_comments
-- ----------------------------
DROP TABLE IF EXISTS `t_user_comments`;
CREATE TABLE `t_user_comments` (
  `id` int(16) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `ctype` int(16) DEFAULT NULL COMMENT '文章类型，0教程1提问2灵感3心得体会',
  `fid` int(16) DEFAULT NULL COMMENT '评论的对象的ID',
  `uid` int(16) DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL COMMENT '评论',
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `status` int(16) NOT NULL DEFAULT '0' COMMENT '状态，0正常1删除',
  `remark` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
