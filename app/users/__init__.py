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
            "Version": "1.0.4",
            "info":"新增了一些BUG，修改了时间显示，新增了图片的上传和读取接口"
        }
    return setcors(data=data,msg="查询成功",status=200)