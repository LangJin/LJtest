# -*- coding:utf-8 -*-
__author__ = 'LangJin'

# 开发环境
class DevelopConfig:
    DEBUG = True
    JSON_AS_ASCII = False #json 中文支持
    BABEL_DEFAULT_LOCALE = 'zh'
    SECRET_KEY = "ssssdddd"    # SESSION配置


# 线上发布环境
class ProductionConfig:
    DEBUG = False
    JSON_AS_ASCII = False #json 中文支持
    BABEL_DEFAULT_LOCALE = 'zh'
    SECRET_KEY = "ssssdddd"    # SESSION配置


flask_config = {
    "DevelopConfig": DevelopConfig,
    "ProductionConfig": ProductionConfig
    }

db_config = {
    # 'host': '192.168.0.103',
    'host': '192.144.148.91',
    'port': 3306,
    'user': 'ljtest',
    'password': '123456',
    'db': 'ljtestdb',
    'charset': 'utf8mb4'
}