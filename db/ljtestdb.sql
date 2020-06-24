/*
Navicat MySQL Data Transfer

Source Server         : 浪晋的腾讯云
Source Server Version : 50726
Source Host           : 192.144.148.91:3306
Source Database       : ljtestdb

Target Server Type    : MYSQL
Target Server Version : 50726
File Encoding         : 65001

Date: 2020-03-20 16:09:31
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
  `userinfo` varchar(255) DEFAULT NULL COMMENT '个性签名',
  `headpic` varchar(255) DEFAULT '/static/images/headpic/headimg.jpg' COMMENT '头像',
  `phone` varchar(255) DEFAULT NULL,
  `sex` varchar(255) DEFAULT NULL,
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '0正常1删除2拉黑',
  `remark` varchar(255) DEFAULT NULL COMMENT '昵称',
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='用户表';

-- ----------------------------
-- Table structure for t_article
-- ----------------------------
DROP TABLE IF EXISTS `t_article`;
CREATE TABLE `t_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL COMMENT '题目',
  `brief` varchar(255) DEFAULT NULL,
  `content` text COMMENT '内容',
  `ximg` varchar(255) NOT NULL DEFAULT 'ximg.jpg' COMMENT '图片显示',
  `tags` varchar(255) DEFAULT NULL COMMENT '分类',
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '状态说明：0正常，1删除，2禁用',
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `uid` int(11) DEFAULT NULL COMMENT '用户id',
  `goods` int(16) NOT NULL DEFAULT '0' COMMENT '点赞数量',
  `collections` int(16) NOT NULL DEFAULT '0' COMMENT '收藏数量',
  `follows` int(16) NOT NULL DEFAULT '0' COMMENT '关注数量',
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63021 DEFAULT CHARSET=utf8 COMMENT='心得体会';

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
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=245 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_content_tags
-- ----------------------------
DROP TABLE IF EXISTS `t_content_tags`;
CREATE TABLE `t_content_tags` (
  `id` int(16) NOT NULL AUTO_INCREMENT,
  `ctype` int(16) NOT NULL COMMENT '文章类型，0教程1提问2灵感3心得体会',
  `tags` varchar(255) NOT NULL COMMENT '标签',
  `status` int(16) NOT NULL DEFAULT '0' COMMENT '状态0正常、1删除，2禁用',
  `uid` int(16) DEFAULT '0',
  `remark` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_coures
-- ----------------------------
DROP TABLE IF EXISTS `t_coures`;
CREATE TABLE `t_coures` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL COMMENT '教程标题',
  `brief` varchar(255) DEFAULT NULL,
  `content` text COMMENT '内容',
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '状态说明：0正常，1删除，2禁用',
  `uid` int(255) DEFAULT NULL COMMENT '管理员ID',
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `ximg` varchar(255) NOT NULL DEFAULT 'ximg.jpg' COMMENT '显示的图片',
  `tags` varchar(255) DEFAULT NULL COMMENT '分类',
  `goods` int(16) DEFAULT '0' COMMENT '点赞数量',
  `collections` int(16) DEFAULT '0' COMMENT '收藏数量',
  `follows` int(16) NOT NULL DEFAULT '0' COMMENT '关注数量',
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=utf8 COMMENT='教程表';

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
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=193 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_inspirer
-- ----------------------------
DROP TABLE IF EXISTS `t_inspirer`;
CREATE TABLE `t_inspirer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text NOT NULL,
  `uid` int(11) DEFAULT NULL COMMENT '这是t_user表的id',
  `ximg` varchar(255) NOT NULL DEFAULT 'ximg.jpg',
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '状态说明：0正常，1删除，2禁用',
  `author` varchar(255) DEFAULT NULL,
  `goods` int(16) DEFAULT '0' COMMENT '点赞数量',
  `collections` int(16) DEFAULT '0' COMMENT '收藏数量',
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1774 DEFAULT CHARSET=utf8 COMMENT='灵光一闪';

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
  `fstatus` int(16) NOT NULL DEFAULT '1',
  `remark` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_questions
-- ----------------------------
DROP TABLE IF EXISTS `t_questions`;
CREATE TABLE `t_questions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL COMMENT '问题题目',
  `brief` varchar(255) DEFAULT NULL COMMENT '简介',
  `content` text COMMENT '内容',
  `tags` varchar(255) DEFAULT NULL COMMENT '问题分类',
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `goods` int(11) DEFAULT '0' COMMENT '点赞数量',
  `collections` int(11) DEFAULT '0' COMMENT '收藏数量',
  `follows` int(16) NOT NULL DEFAULT '0' COMMENT '关注数量',
  `status` int(11) NOT NULL DEFAULT '0' COMMENT '状态说明：0正常，1删除，2禁用',
  `ximg` varchar(255) NOT NULL DEFAULT 'ximg.jpg' COMMENT '显示的图片',
  `uid` int(11) NOT NULL COMMENT '提问人ID',
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1902 DEFAULT CHARSET=utf8 COMMENT='交流讨论表';

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
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=119 DEFAULT CHARSET=utf8;

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
  `status` int(11) DEFAULT '0' COMMENT '状态，0正常，1删除',
  `remark` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='轮播图表';

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL COMMENT '账号',
  `password` varchar(255) NOT NULL COMMENT '密码',
  `mb` json DEFAULT NULL COMMENT '密保',
  `nickname` varchar(255) DEFAULT NULL COMMENT '昵称',
  `titlepic` varchar(255) DEFAULT 'titleimg.jpg' COMMENT '主页背景图',
  `headpic` varchar(255) DEFAULT 'headimg.jpg' COMMENT '头像',
  `phone` varchar(255) DEFAULT NULL COMMENT '电话号码',
  `sex` varchar(255) DEFAULT '保密' COMMENT '性别',
  `job` varchar(255) DEFAULT '风和自由' COMMENT '职业',
  `email` varchar(255) DEFAULT NULL,
  `weixin` varchar(255) DEFAULT NULL,
  `QQ` varchar(255) DEFAULT NULL,
  `userinfo` varchar(255) DEFAULT '没有签名最有个性' COMMENT '个人签名',
  `address` varchar(255) DEFAULT NULL COMMENT '地址',
  `status` varchar(255) NOT NULL DEFAULT '0' COMMENT '0正常1删除2锁定3冻结',
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=103466 DEFAULT CHARSET=utf8 COMMENT='用户表';

-- ----------------------------
-- Table structure for t_user_comments
-- ----------------------------
DROP TABLE IF EXISTS `t_user_comments`;
CREATE TABLE `t_user_comments` (
  `id` int(16) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `ctype` int(16) DEFAULT NULL COMMENT '文章类型，0教程1提问2灵感3心得体会',
  `fid` int(16) DEFAULT NULL COMMENT '评论的对象的ID',
  `uid` int(16) DEFAULT NULL COMMENT '用户ID',
  `comment` text COMMENT '评论的内容',
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `status` int(16) NOT NULL DEFAULT '0' COMMENT '状态，0正常1删除',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4578 DEFAULT CHARSET=utf8 COMMENT='用户评论表';

-- ----------------------------
-- Table structure for t_user_follows
-- ----------------------------
DROP TABLE IF EXISTS `t_user_follows`;
CREATE TABLE `t_user_follows` (
  `id` int(16) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `fid` int(16) NOT NULL COMMENT '被关注人id',
  `uid` int(16) NOT NULL COMMENT '用户id',
  `status` int(16) NOT NULL DEFAULT '0' COMMENT '0关注，1没关注',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  `createtime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8 COMMENT='用户关注和粉丝表';

-- ----------------------------
-- Table structure for t_user_mbq
-- ----------------------------
DROP TABLE IF EXISTS `t_user_mbq`;
CREATE TABLE `t_user_mbq` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(255) NOT NULL COMMENT '密保问题',
  `uid` int(11) NOT NULL COMMENT '用户ID',
  `status` int(16) NOT NULL DEFAULT '0' COMMENT '状态，0正常，1删除',
  `remark` varchar(255) DEFAULT NULL,
  `createtime` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='密保问题表';
