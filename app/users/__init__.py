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
            "Version": "1.0.7",
            "info":"修改了一些BUG，新增了更多的BUG",
            "Version": "1.0.10",
            "info":"大幅度的修改了后台的接口，和部分BUG"
        }
    return setcors(data=data,msg="查询成功",status=200)