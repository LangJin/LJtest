# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from config import config
from flask import Flask
from .users import userbp
from .errors import errorbp




def create_app(config_name="Develop"):
    '''
    工厂方法
    '''
    app = Flask(__name__)
    app.config.update(config[config_name])
    app.register_blueprint(userbp)  # 注册蓝本
    app.register_blueprint(errorbp)  # 注册蓝本
    return app
