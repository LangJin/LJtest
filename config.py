# -*- coding:utf-8 -*-
__author__ = 'LangJin'

DEBUG = True
JSON_AS_ASCII = False  # 接口返回的json支持中文
BABEL_DEFAULT_LOCALE = "zh"
SECRET_KEY = "Sm9obiBTY2hyb20ga2lja3MgYXNz"  # SESSION配置
THREADED = True  # 开启多线程


db_config = {
    'host': '192.144.148.91',
    'port': 3306,
    'user': 'root',
    'password': '1qaz!QAZ',
    'db': 'ljtestdb',
    'charset': 'utf8mb4'
}

