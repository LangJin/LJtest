# -*- coding:utf-8 -*-
__author__ = 'LangJin'

import os, hashlib
from flask import jsonify,make_response,session


def create_token():
    '''
    生成登陆后的token，格式如下：\n
    "eca7f38788d4764959919b46c61005038cf37f68"
    '''
    return hashlib.sha1(os.urandom(64)).hexdigest()

def encryption(username,password,role):
    '''
    说明：密码的加密算法,role是角色\n
    用法:encryption("用户名","明文密码","user")
    '''
    md5 = hashlib.md5()
    md5.update(password.encode("utf8")+username.encode("utf8")+keys.get(role).encode("utf8"))
    password = md5.hexdigest()
    return password

def checkusername(username):
    '''
    检查账号是否满足用户需求
    '''
    if username != None:
        if len(username) >= 6 and len(username) <= 12:
            for i in username:
                if i not in "0123456789qazwsxedcrfvtgbyhnujmikolp":
                    return "账号仅能由数字和字母组成！"
            return True
        else:
            return "账号长度必须大于等于6位，并且小于等于12位"
    else:
        return "账号不能为空！"


def checkpasswd(password):
    '''
    检查密码是否符合规范
    '''
    if password != None:
        if len(password) >= 8 and len(password) <= 16:
            return True
        else:
            return "密码长度必须大于等于8位，并且小于等于16位"
    else:
        return "密码不能为空！"

def checkloginstatus(session,token):
    '''
    检查用户的登录状态
    '''
    userinfo = session.get("userinfo")
    if userinfo != None and token != None:
        tokenid = userinfo.get("token")
        if tokenid == token:
            return True
        else:
            return False
    else:
        return False



def setcors(data):
    '''
    解决跨域问题
    '''
    res = make_response(jsonify(data))
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Method'] = '*'
    res.headers['Access-Control-Allow-Headers'] = '*'
    return res