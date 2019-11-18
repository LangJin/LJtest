# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from config import config
from flask import Flask
from .users import userbp
from .errors import errorbp
from .admins import adminbp



def create_app(config_name="Develop"):
    '''
    工厂方法
    '''
    app = Flask(__name__,static_url_path='')  # static_url_path，强制指定静态资源的访问路径，解决二级路径访问静态资源404的问题
    app.config.update(config[config_name])
    app.register_blueprint(userbp)  # 注册蓝本
    app.register_blueprint(errorbp)  # 注册蓝本
    app.register_blueprint(adminbp)  # 注册蓝本

    return app
