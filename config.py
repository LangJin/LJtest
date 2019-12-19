# -*- coding:utf-8 -*-
__author__ = 'LangJin'

# 开发环境
class DevelopConfig:
    DEBUG = True
    JSON_AS_ASCII = False #json 中文支持
    BABEL_DEFAULT_LOCALE = 'zh'
    SECRET_KEY = "ssssdddd"    # SESSION配置
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024 # 2MB  限制文件大小



# 线上发布环境
class ProductionConfig:
    DEBUG = False
    JSON_AS_ASCII = False #json 中文支持
    BABEL_DEFAULT_LOCALE = 'zh'
    SECRET_KEY = "ssssdddd"    # SESSION配置
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024 # 2MB  限制文件大小




flask_config = {
    "DevelopConfig": DevelopConfig,
    "ProductionConfig": ProductionConfig
    }

UPLOAD_FOLDER = './app/static/images'  # 上传的文件路径


db_config = {
    # 'host': '192.168.0.103',
    'host': '192.144.148.91',
    'port': 3306,
    'user': 'ljtest',
    'password': '123456',
    'db': 'ljtestdb',
    'charset': 'utf8mb4'
}