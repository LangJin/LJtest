# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Blueprint
from ..utils.othertools import setcors

userbp = Blueprint("user", __name__)

from . import home,user,upload


@userbp.route("/showversion")
def showversion():
    '''
    查看系统版本
    '''
    data = {
            "Version": "1.0.3",
            "info":"1、修改了禅道上提出的一堆BUG。\n\
                2、优化了代码，增加了部分BUG。\n\
                3、新增了后台管理的部分接口，详情请看接口文档"
        }
    return setcors(data=data,msg="查询成功",status=200)