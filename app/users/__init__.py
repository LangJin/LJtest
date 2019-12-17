# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Blueprint
from ..utils.othertools import setcors

userbp = Blueprint("user", __name__)

from . import home,user


@userbp.route("/showversion")
def showversion():
    '''
    查看系统版本
    '''
    data = {
        "status":200,
        "data":{
            "Version": "1.0.1",
            "info":"1、修改首页的获取各种数据num为非数字报错的BUG。"
        },
        "msg":"查询成功！"
    }
    return setcors(data)