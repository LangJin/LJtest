# -*- coding:utf-8 -*-
__author__ = 'LangJin'

from flask import request,session,make_response
from . import adminbp
from ..utils.dbtools import Db
from config import db_config
from ..utils.othertools import checkuserinfo,create_token,encryption,setcors,checkloginstatus,checkContentType,is_number,checkvalueisNone
# from werkzeug import secure_filename


db = Db(db_config)



@adminbp.route("/adminlogin",methods=["post"])
def adminlogin():
    '''
    管理员登录接口\n
    获取json格式的数据进行处理
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    else:
        userinfo = request.get_json()
        username = userinfo.get("username")
        password = userinfo.get("password")
        userregmsg = checkuserinfo(username,password)
        if userregmsg is True:
            sql = "select * from t_admin where status = 0 and username = '{}'".format(username)
            res = db.query(sql)
            if len(res) != 1:
                return setcors(msg="账号不存在或者账号异常")
            else:
                # password = encryption(username,password,"admin")
                if password == res[0].get("password"):
                    token = create_token()
                    session.clear()
                    session["userinfo"] = {"token":token,"uid":res[0]["id"],"nickname":res[0]["nickname"]}
                    userinfo = {
                        "nickname":res[0]["nickname"],
                        "uid":res[0]["id"],
                        "headpic":res[0]["headpic"]
                    }
                    data = {}
                    data["userinfo"] = userinfo
                    data["token"] = token
                    return setcors(msg="登录成功！",data=data,status=200)
                else:
                    return setcors(msg="密码错误")
        else:
            return setcors(msg=userregmsg)


# 教程的增删改查
@adminbp.route("/coureslist",methods=["get"])
def coureslist():
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    token = request.headers.get("token")
    pagenum = int(request.args.get("pagenum"))
    endnum = 10
    if pagenum == 1:
        startnum = 0
    else:
        startnum = (pagenum-1)*10
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        couresnum = db.query("select count(*) couresnum  from t_coures where status = 0;")
        res = db.query("select * from t_coures where status = 0 limit {},{};".format(startnum,endnum))
        data = {
            "coureslist":res,
            "couresnum":couresnum[0].get("couresnum")
        }
        return setcors(data=data,status=200)
    else:
        return setcors(msg=loginstatus)


# 灵感的搜索、删除
@adminbp.route("/inspirlist",methods=["get"])
def inspirlist():
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    pagenum = int(request.args.get("pagenum"))
    endnum = 10
    if pagenum == 1:
        startnum = 0
    else:
        startnum = (pagenum-1)*10
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        inspirnum = db.query("select count(*) inspirnum  from t_inspirer where status = 0;")
        res = db.query("select * from t_inspirer where status = 0 limit {},{};".format(startnum,endnum))
        data = {
            "inspirlist":res,
            "inspirnum":inspirnum[0].get("inspirnum")
        }
        return setcors(data=data,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/inspirdelete",methods=["post"])
def inspirdelete():
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    dlist = tuple(requestdata.get("dlist"))
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        res = db.commit("update t_inspirer set status = 1 where id in {};".format(dlist))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)



@adminbp.route("/inspirupdate",methods=["post"])
def inspirupdate():
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    iid = requestdata.get("iid")
    content = requestdata.get("content")
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        dbres = db.commit("update t_inspirer set content = '{}' where id = {} ;".format(content,iid))
        return setcors(data=dbres,status=200)
    else:
        return setcors(msg=loginstatus)


# 文章的搜索删除
@adminbp.route("/articlelist",methods=["get"])
def articlelist():
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    pagenum = int(request.args.get("pagenum"))
    endnum = 10
    if pagenum == 1:
        startnum = 0
    else:
        startnum = (pagenum-1)*10
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        articlenum = db.query("select count(*) articlenum  from t_article where status = 0 ;")
        res = db.query("select * from t_article where status = 0 limit {},{};".format(startnum,endnum))
        data = {
            "articlelist":res,
            "articlenum":articlenum[0].get("articlenum")
        }
        return setcors(data=data,status=200)
    else:
        return setcors(msg=loginstatus)

@adminbp.route("/articledelete",methods=["post"])
def articledelete():
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    dlist = tuple(requestdata.get("dlist"))
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        res = db.commit("update t_article set status = 1 where id in {};".format(dlist))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


# 问题的搜索删除
@adminbp.route("/questionslist",methods=["get"])
def questionslist():
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    pagenum = int(request.args.get("pagenum"))
    endnum = 10
    if pagenum == 1:
        startnum = 0
    else:
        startnum = (pagenum-1)*10
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        questionsnum = db.query("select count(*) questionsnum  from t_questions where status = 0 ;")
        res = db.query("select * from t_questions where status = 0 limit {},{};".format(startnum,endnum))
        data = {
            "questionslist":res,
            "questionsnum":questionsnum[0].get("questionsnum")
        }
        return setcors(data=data,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/questionsdelete",methods=["post"])
def questionsdelete():
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    dlist = tuple(requestdata.get("dlist"))
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        res = db.commit("update t_questions set status = 1 where id in {};".format(dlist))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)

# 用户的搜索删除
@adminbp.route("/userlist",methods=["get"])
def userlist():
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    pagenum = int(request.args.get("pagenum"))
    endnum = 10
    if pagenum == 1:
        startnum = 0
    else:
        startnum = (pagenum-1)*10
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        allusernum = db.query("select count(*) usernum  from t_user where status = 0 ;")
        res = db.query("select * from t_user where status = 0 limit {},{};".format(startnum,endnum))
        data = {
            "userlist":res,
            "usernum":allusernum[0].get("usernum")
        }
        return setcors(data=data,status=200)
    else:
        return setcors(msg=loginstatus)

@adminbp.route("/usersdelete",methods=["post"])
def usersdelete():
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    dlist = tuple(requestdata.get("dlist"))
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        res = db.commit("update t_user set status = 1 where id in {};".format(dlist))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)