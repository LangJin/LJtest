# -*- coding:utf-8 -*-
__author__ = 'LangJin'

import os



DevelopConfig = {
    "DEBUG": True,
    "HOST": "0.0.0.0",
    "JSON_AS_ASCII": False,  # 接口返回的json支持中文
    "BABEL_DEFAULT_LOCALE": "zh",
    "SECRET_KEY": os.urandom(24),  # SESSION配置
    "THREADED": True  # 开启多线程
}

ProductionConfig = {
    "DEBUG": False,
    "HOST": "0.0.0.0",
    "JSON_AS_ASCII": False,  # 接口返回的json支持中文
    "BABEL_DEFAULT_LOCALE": "zh",
    "SECRET_KEY": os.urandom(24),  # SESSION配置
    "THREADED":True
}

config = {
    "Develop": DevelopConfig,
    "Production": ProductionConfig
}

db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'lux',
    'charset': 'utf8mb4'
}

keys = {
    "user":"sb250",
    "admin":"god666"
}
