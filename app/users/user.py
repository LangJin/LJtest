# -*- coding:utf-8 -*-
__author__ = 'LangJin'

from flask import jsonify,session,request
from . import userbp
from ..utils.mysqltools import query,commit
from ..utils.othertools import create_token,encryption


@userbp.route("/user/login",methods=["post"])
def userlogin():
    '''
    用户登录接口\n
    获取json格式的数据进行处理
    '''
    userinfo = request.get_json()
    username = userinfo.get("username")
    password = userinfo.get("password")
    if len(username) != 0 and len(password) != 0:
        sql = "select * from t_user where username = '{}'".format(username)
        res = query(sql)
        data = {}
        if len(res) != 1:
            data["msg"] = "数据异常或者用户不存在！"
            data["data"] = None
        else:
            password = encryption(username,password,"user")
            if password == res[0].get("password"):
                token = create_token()
                sql = "update t_user set token = '{token}' where id = {id};".format(token=token,id=res[0].get("id"))
                msg = commit(sql)
                session.clear()
                session["username"] = username
                session["token"] = token
                data["msg"] = "登录成功！"
                data["data"] = {}
                data["data"]["token"] = token
                data["data"]["status"] = msg
            else:
                data["msg"] = "密码错误！"
    else:
        data = {
            "msg":"账号为空！"
        }
    return jsonify(data)


@userbp.route("/user/regist",methods=["post"])
def regist():
    '''
    用户注册接口\n
    获取json格式的数据进行处理
    '''
    userinfo = request.get_json()
    username = userinfo.get("username")
    password = userinfo.get("password")
    sql = "select * from t_user where username = '{}'".format(username)
    res = query(sql)
    data = {}
    if len(res) != 0:
        data["msg"] = "用户名已存在，请重新设置！"
        data["data"] = None
    else:
        password = encryption(username,password,"user")
        sql = "insert into t_user (username,password) values ('{}','{}');".format(username,password)
        msg = commit(sql)
        data["msg"] = "注册成功！"
        data["data"] = {}
        data["data"]["status"] = msg
    return jsonify(data)


