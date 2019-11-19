# -*- coding:utf-8 -*-
__author__ = 'LangJin'

from flask import jsonify,request
from . import userbp
from ..utils.dbtools import Db
from config import db_config
from ..utils.othertools import checkusername,checkpasswd,create_token

db = Db(db_config)


@userbp.route("/regist",methods=["post","get"])
def regist():
    '''
    用户注册接口\n
    获取json格式的数据进行处理
    '''
    if request.method == "POST":
        userinfo = request.get_json()
        username = userinfo.get("username")
        password = userinfo.get("password")
        usernamemsg = checkusername(username)
        data = {}
        if usernamemsg is True:
            sql = "select * from t_user where username = '{}'".format(username)
            res = db.query(sql)
            if len(res) != 0:
                data["msg"] = "用户名已存在，请重新设置！"
                data["data"] = None
            else:
                # password = encryption(username,password,"user")
                passwd = checkpasswd(password)
                if passwd is True:
                    sql = "insert into t_user (username,password) values ('{}','{}');".format(username,password)
                    msg = db.commit(sql)
                    data["msg"] = "注册成功！"
                    data["data"] = {}
                    data["data"]["status"] = msg
                else:
                    data["msg"] = passwd
            return jsonify(data)
        else:
            data["msg"] = usernamemsg
            return jsonify(data)
        
    else:
        return "注册界面"


@userbp.route("/login",methods=["post","get"])
def userlogin():
    '''
    用户登录接口\n
    获取json格式的数据进行处理
    '''
    if request.method == "POST":
        userinfo = request.get_json()
        username = userinfo.get("username")
        password = userinfo.get("password")
        if len(username) != 0 and len(password) != 0:
            sql = "select * from t_user where username = '{}'".format(username)
            res = db.query(sql)
            data = {}
            if len(res) != 1:
                data["msg"] = "数据异常或者用户不存在！"
                data["data"] = None
            else:
                # password = encryption(username,password,"user")
                if password == res[0].get("password"):
                    token = create_token()
                    sql = "update t_user set token = '{token}' where id = {id};".format(token=token,id=res[0].get("id"))
                    msg = db.commit(sql)
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
    else:
        return "登录界面"


@userbp.route("/user/question",methods=["post"])
def question():
    questiondata = request.get_json()
    token = request.headers.get("token")
    title = questiondata.get("title")
    tags = questiondata.get("tags")
    content = questiondata.get("content")
    resdata = {}
    if token != None:
        res = db.query("select id,username from t_user where token = '{}';".format(token))
        if len(res) != 1:
            resdata["msg"] = "无效token"
            return jsonify(resdata)
        else:
            # print(res)
            uid = res[0]["id"]
            author = res[0]["username"]
            dbres = db.commit("insert into t_questions (title,content,tags,uid) values ('{}','{}','{}',{});".format(title,content,tags,uid))
            resdata["status"] = dbres
            resdata["msg"] = "提问成功"
            return jsonify(resdata)
    else:
        resdata["msg"] = "未登录"
        return jsonify(resdata)
