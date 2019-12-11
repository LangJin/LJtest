# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Flask
from .users import userbp
from .errors import errorbp




def create_app():
    '''
    工厂方法
    '''
    app = Flask(__name__,instance_relative_config=True)
    # app.config.from_object("config")
    app.secret_key = "cdhhhhhhhkjdn"
    app.config.from_pyfile('config.py')
    app.register_blueprint(userbp)  # 注册蓝本
    app.register_blueprint(errorbp)  # 注册蓝本
    return app

