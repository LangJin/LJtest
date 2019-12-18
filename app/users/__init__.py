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
            "Version": "1.0.2",
            "info":"1、修改了禅道上提出的一堆BUG。\n\
                2、优化了代码，增加了部分BUG。"
        }
    return setcors(data=data,msg="查询成功",status=200)