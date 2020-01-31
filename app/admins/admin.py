# -*- coding:utf-8 -*-
__author__ = 'LangJin'

from flask import request,session,make_response
from . import adminbp
from ..utils.dbtools import Db
from config import db_config
from ..utils.othertools import checkuserinfo,create_token,encryption,setcors,checkadminloginstatus,checkContentType,is_number,checkvalueisNone,checklistid
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
                    session["admininfo"] = {"token":token,"uid":res[0]["id"],"nickname":res[0]["nickname"]}
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
    '''
    后台教程列表
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    token = request.headers.get("token")
    pagenum = request.args.get("pagenum")
    pagenummsg = is_number(pagenum)
    if pagenummsg != True:
        return setcors(msg=pagenummsg)
    else:
        pagenum = int(pagenum)
    endnum = 10
    if pagenum == 1:
        startnum = 0
    else:
        startnum = (pagenum-1)*10
    loginstatus = checkadminloginstatus(session,token)
    if loginstatus is True:
        couresnum = db.query("select  count(*) couresnum  from t_coures where status = 0;")
        res = db.query("select id,title,brief,content,ximg,tags,author,goods,collections,follows,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_coures where status = 0 limit {},{};".format(startnum,endnum))
        data = {
            "coureslist":res,
            "couresnum":couresnum[0].get("couresnum")
        }
        return setcors(data=data,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/couresnew",methods=["post"])
def couresnew():
    '''
    后台新增教程
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    title = requestdata.get("title")
    brief = requestdata.get("brief")
    tags = requestdata.get("tags")
    content = requestdata.get("content")
    valuemsg = checkvalueisNone([title,brief,tags,content])
    if valuemsg != True:
        return setcors(msg=valuemsg)
    token = request.headers.get("token")
    loginstatus = checkadminloginstatus(session,token)
    if loginstatus is True:
        uid = session["admininfo"]["uid"]
        author = session["admininfo"]["nickname"]
        dbres = db.commit("insert into t_coures (title,brief,content,tags,uid,author) values ('{}','{}','{}','{}',{},'{}');".format(title,brief,content,tags,uid,author))
        return setcors(msg=dbres,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/couresupdate",methods=["post"])
def couresupdate():
    '''
    后台修改教程
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    title = requestdata.get("title")
    brief = requestdata.get("brief")
    tags = requestdata.get("tags")
    content = requestdata.get("content")
    cid = requestdata.get("cid")
    valuemsg = checkvalueisNone([title,brief,tags,content,cid])
    if valuemsg != True:
        return setcors(msg=valuemsg)
    token = request.headers.get("token")
    loginstatus = checkadminloginstatus(session,token)
    if loginstatus is True:
        uid = session["admininfo"]["uid"]
        qres = db.query("select * from t_coures where uid ={} and status = 0 and id = {};".format(uid,cid))
        if len(qres) != 0:
            dbres = db.commit("update t_coures set title='{}',brief='{}',tags='{}',content='{}' where id = {};".format(title,brief,tags,content,cid))
            return setcors(msg=dbres,status=200)
        else:
            return setcors(msg="修改的教程不存在")
    else:
        return setcors(msg=loginstatus)

# 灵感的搜索、删除
@adminbp.route("/inspirlist",methods=["get"])
def inspirlist():
    '''
    后台灵感列表
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    pagenum = request.args.get("pagenum")
    pagenummsg = is_number(pagenum)
    if pagenummsg != True:
        return setcors(msg=pagenummsg)
    else:
        pagenum = int(pagenum)
    endnum = 10
    if pagenum == 1:
        startnum = 0
    else:
        startnum = (pagenum-1)*10
    token = request.headers.get("token")
    loginstatus = checkadminloginstatus(session,token)
    if loginstatus is True:
        inspirnum = db.query("select count(*) inspirnum  from t_inspirer where status = 0;")
        res = db.query("select id,content,ximg,author,goods,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_inspirer where status = 0 limit {},{};".format(startnum,endnum))
        data = {
            "inspirlist":res,
            "inspirnum":inspirnum[0].get("inspirnum")
        }
        return setcors(data=data,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/inspirdelete",methods=["post"])
def inspirdelete():
    '''
    后台删除灵感
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    dlist = str(requestdata.get("dlist"))
    listmsg = checklistid(dlist)
    if listmsg != True:
        return setcors(msg=listmsg)
    dlist = dlist[:-1]
    token = request.headers.get("token")
    loginstatus = checkadminloginstatus(session,token)
    if loginstatus is True:
        res = db.commit("update t_inspirer set status = 1 where id in ({});".format(dlist))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)



@adminbp.route("/inspirupdate",methods=["post"])
def inspirupdate():
    '''
    后台修改灵感
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    iid = requestdata.get("iid")
    content = requestdata.get("content")
    token = request.headers.get("token")
    loginstatus = checkadminloginstatus(session,token)
    if loginstatus is True:
        dbres = db.commit("update t_inspirer set content = '{}' where id = {} ;".format(content,iid))
        return setcors(data=dbres,status=200)
    else:
        return setcors(msg=loginstatus)


# 文章的搜索删除
@adminbp.route("/articlelist",methods=["get"])
def articlelist():
    '''
    后台文章列表
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    pagenum = request.args.get("pagenum")
    pagenummsg = is_number(pagenum)
    if pagenummsg != True:
        return setcors(msg=pagenummsg)
    else:
        pagenum = int(pagenum)
    endnum = 10
    if pagenum == 1:
        startnum = 0
    else:
        startnum = (pagenum-1)*10
    token = request.headers.get("token")
    loginstatus = checkadminloginstatus(session,token)
    if loginstatus is True:
        articlenum = db.query("select count(*) articlenum  from t_article where status = 0 ;")
        res = db.query("select id,title,brief,content,ximg,tags,author,goods,collections,follows,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_article where status = 0 limit {},{};".format(startnum,endnum))
        data = {
            "articlelist":res,
            "articlenum":articlenum[0].get("articlenum")
        }
        return setcors(data=data,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/articledelete",methods=["post"])
def articledelete():
    '''
    后台删除文章
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    dlist = str(requestdata.get("dlist"))
    listmsg = checklistid(dlist)
    if listmsg != True:
        return setcors(msg=listmsg)
    dlist = dlist[:-1]
    token = request.headers.get("token")
    loginstatus = checkadminloginstatus(session,token)
    if loginstatus is True:
        res = db.commit("update t_article set status = 1 where id in ({});".format(dlist))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


# 问题的搜索删除
@adminbp.route("/questionslist",methods=["get"])
def questionslist():
    '''
    后台问题列表
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    pagenum = request.args.get("pagenum")
    pagenummsg = is_number(pagenum)
    if pagenummsg != True:
        return setcors(msg=pagenummsg)
    else:
        pagenum = int(pagenum)
    endnum = 10
    if pagenum == 1:
        startnum = 0
    else:
        startnum = (pagenum-1)*10
    token = request.headers.get("token")
    loginstatus = checkadminloginstatus(session,token)
    if loginstatus is True:
        questionsnum = db.query("select count(*) questionsnum  from t_questions where status = 0 ;")
        res = db.query("select id,title,brief,content,ximg,tags,author,goods,collections,follows,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_questions where status = 0 limit {},{};".format(startnum,endnum))
        data = {
            "questionslist":res,
            "questionsnum":questionsnum[0].get("questionsnum")
        }
        return setcors(data=data,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/questionsdelete",methods=["post"])
def questionsdelete():
    '''
    后台删除问题
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    dlist = str(requestdata.get("dlist"))
    listmsg = checklistid(dlist)
    if listmsg != True:
        return setcors(msg=listmsg)
    dlist = dlist[:-1]
    token = request.headers.get("token")
    loginstatus = checkadminloginstatus(session,token)
    if loginstatus is True:
        res = db.commit("update t_questions set status = 1 where id in ({});".format(dlist))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)

# 用户的搜索删除
@adminbp.route("/userlist",methods=["get"])
def userlist():
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    pagenum = request.args.get("pagenum")
    pagenummsg = is_number(pagenum)
    if pagenummsg != True:
        return setcors(msg=pagenummsg)
    else:
        pagenum = int(pagenum)
    endnum = 10
    if pagenum == 1:
        startnum = 0
    else:
        startnum = (pagenum-1)*10
    token = request.headers.get("token")
    loginstatus = checkadminloginstatus(session,token)
    if loginstatus is True:
        allusernum = db.query("select count(*) usernum  from t_user where status = 0 ;")
        res = db.query("select id,nickname,titlepic,headpic,phone,sex,job,email,weixin,QQ,userinfo,address,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_user where status = 0 limit {},{};".format(startnum,endnum))
        data = {
            "userlist":res,
            "usernum":allusernum[0].get("usernum")
        }
        return setcors(data=data,status=200)
    else:
        return setcors(msg=loginstatus)

@adminbp.route("/usersdelete",methods=["post"])
def usersdelete():
    '''
    后台删除用户
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    dlist = str(requestdata.get("dlist"))
    listmsg = checklistid(dlist)
    if listmsg != True:
        return setcors(msg=listmsg)
    dlist = dlist[:-1]
    token = request.headers.get("token")
    loginstatus = checkadminloginstatus(session,token)
    if loginstatus is True:
        res = db.commit("update t_user set status = 1 where id in ({});".format(dlist))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)