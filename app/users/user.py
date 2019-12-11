# -*- coding:utf-8 -*-
__author__ = 'LangJin'

from flask import jsonify,request,render_template,session
from . import userbp
from ..utils.dbtools import Db
from config import db_config
from ..utils.othertools import checkusername,checkpasswd,create_token

db = Db(db_config)


@userbp.route("/regist",methods=["post"])
def regist():
    '''
    用户注册接口\n
    获取json格式的数据进行处理
    '''

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



@userbp.route("/login",methods=["post","get"])
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
        res = db.query(sql)
        data = {}
        if len(res) != 1:
            data["msg"] = "数据异常或者用户不存在！"
            data["data"] = None
        else:
            # password = encryption(username,password,"user")
            if password == res[0].get("password"):
                token = create_token()
                session["token"] = token
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



@userbp.route("/question/new",methods=["post"])
def question():
    '''
    提问接口
    '''
    questiondata = request.get_json()
    token = request.headers.get("token")
    title = questiondata.get("title")
    brief = questiondata.get("brief")
    tags = questiondata.get("tags")
    content = questiondata.get("content")
    uid = questiondata.get("uid")
    resdata = {}
    if session.get("token") != None and session.get("token") == token:
        dbres = db.commit("insert into t_questions (title,brief,content,tags,uid) values ('{}','{}','{}','{}',{});".format(title,brief,content,tags,uid))
        resdata["status"] = dbres
        resdata["msg"] = "提问成功"
        return jsonify(resdata)
    else:
        resdata["msg"] = "未登录"
        return jsonify(resdata)
    

@userbp.route("/question/update",methods=["post"])
def questionupdate():
    '''
    修改提问接口
    '''
    questiondata = request.get_json()
    token = request.headers.get("token")
    title = questiondata.get("title")
    brief = questiondata.get("brief")
    tags = questiondata.get("tags")
    content = questiondata.get("content")
    uid = questiondata.get("uid")
    resdata = {}
    if session.get("token") != None and session.get("token") == token:
        dbres = db.commit("insert into t_questions (title,brief,content,tags,uid) values ('{}','{}','{}','{}',{});".format(title,brief,content,tags,uid))
        resdata["status"] = dbres
        resdata["msg"] = "提问成功"
        return jsonify(resdata)
    else:
        resdata["msg"] = "未登录"
        return jsonify(resdata)