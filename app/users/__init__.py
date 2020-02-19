# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Blueprint
from ..utils.othertools import setcors

userbp = Blueprint("user", __name__)

from . import home,user,upload,userinfo


@userbp.route("/showversion")
def showversion():
    '''
    查看系统版本
    '''
    data = {
            "Version": "1.0.9",
            "info":"新增了修改密码和密保相关的接口，写了一些新的BUG。"
        }
    return setcors(data=data,msg="查询成功",status=200)