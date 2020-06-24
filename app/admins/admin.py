# -*- coding:utf-8 -*-
__author__ = 'LangJin'

from flask import request,session,make_response
from . import adminbp
from ..utils.dbtools import Db,RedisDb
from config import db_config,redis_aconfig
from ..utils.othertools import checkuserinfo,create_token,encryption,setcors,checkContentType,is_number,checkvalueisNone,checklistid
from ..utils.othertools import encryptiontoken,checkadminloginstatus,checkurl,checkvaluelen
# from werkzeug import secure_filename

db = Db(db_config)
redisdb = RedisDb(redis_aconfig) 



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
                    redisdata = {}
                    redisdata["admininfo"] = {"token":token,"uid":res[0]["id"],"nickname":res[0]["nickname"]}
                    resbool = redisdb.setredisvalue(username,redisdata)
                    userinfo = {
                        "nickname":res[0]["nickname"],
                        "uid":res[0]["id"],
                        "headpic":res[0]["headpic"]
                    }
                    data = {"status":resbool}
                    data["userinfo"] = userinfo
                    data["token"] = encryptiontoken(username,token)
                    return setcors(msg="登录成功！",data=data,status=200)
                else:
                    return setcors(msg="密码错误")
        else:
            return setcors(msg=userregmsg)


"""
轮播图管理
状态，0正常，1，删除，2禁用
"""
@adminbp.route("/titleimglist",methods=["get"])
def titleimglist():
    '''
    获取轮播图列表
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        tid = request.args.get("id")
        if tid == "" or tid == None:
            res = db.query("select id,title,imghost,rurl,status,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_title_img where status != 1;")
            return setcors(data=res,status=200)
        else:
            idmsg = is_number(tid)
            if idmsg != True:
                return setcors(msg=idmsg)
            res = db.query("select id,title,imghost,rurl,status,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_title_img where status != 1 and id = {};".format(tid))
            if len(res) == 0:
                return setcors(msg="输入的id不存在！")
            return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/newtitleimg",methods=["post"])
def newtitleimg():
    '''
    新增轮播图
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    title = requestdata.get("title")
    if title == None or title == "":
        return setcors(msg="title不能为空！")
    imghost = requestdata.get("imghost")
    if imghost == None or imghost == "":
        return setcors(msg="图片不能为空！")
    rurl = requestdata.get("rurl")
    urlmsg = checkurl(rurl)
    if urlmsg != True:
        return setcors(msg=urlmsg)
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("insert into t_title_img (title,imghost,rurl) values ('{}','{}','{}');".format(title,imghost,rurl))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/updatetitleimg",methods=["post"])
def updatetitleimg():
    '''
    修改轮播图
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    title = requestdata.get("title")
    if title == None or title == "":
        return setcors(msg="title不能为空！")
    imghost = requestdata.get("imghost")
    if imghost == None or imghost == "":
        return setcors(msg="图片不能为空！")
    rurl = requestdata.get("rurl")
    urlmsg = checkurl(rurl)
    if urlmsg != True:
        return setcors(msg=urlmsg)
    tid = requestdata.get("tid")
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_title_img set title = '{}',imghost = '{}',rurl = '{}' where id = {};".format(title,imghost,rurl,tid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/settitleimgstatus",methods=["get"])
def settitleimgstatus():
    '''
    禁用/启用轮播图
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    tid = request.args.get("id")
    idmsg = is_number(tid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_title_img set status = (case when status = 2 then 0 else 2 end) where id = {};".format(tid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/deletetitleimg",methods=["get"])
def deletetitleimg():
    '''
    删除轮播图
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    tid = request.args.get("id")
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_title_img set status = 1 where id = {};".format(tid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


"""
用户管理
状态，0正常，1删除，2锁定，3冻结
"""
@adminbp.route("/userlist",methods=["get"])
def userlist():
    '''
    获取用户列表接口
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
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        allusernum = db.query("select count(*) usernum  from t_user where status != 1;")[0].get("usernum")
        res = db.query("select id,nickname,titlepic,headpic,phone,sex,job,email,weixin,QQ,userinfo,address,status,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_user where status != 1 limit {},{};".format(startnum,endnum))
        data = {
            "userlist":res,
            "usernum":allusernum
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
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_user set status = 1 where id in ({});".format(dlist))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)



@adminbp.route("/usersfreeze",methods=["post"])
def usersfreeze():
    '''
    后台冻结/解冻用户
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
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_user set status = (case when status = 3 then 0 else 3 end)  where id in ({});".format(dlist))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/usersfind",methods=["post"])
def usersfind():
    '''
    后台查找用户
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    search = requestdata.get("search")
    if search == None or search == "":
        return setcors(msg="搜索内容不能为空！")
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.query("select id,nickname,titlepic,headpic,phone,sex,job,email,weixin,QQ,userinfo,address,status,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_user where status !=1 and username like '%{}%' or nickname like '%{}%';".format(search,search))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)



"""
教程管理
状态说明：0正常，1删除，2禁用
"""
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
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        couresnum = db.query("select  count(*) couresnum  from t_coures where status != 1;")
        res = db.query("select id,title,brief,content,status,ximg,tags,author,goods,collections,follows,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_coures where status != 1 limit {},{};".format(startnum,endnum))
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
    titleimg = checkvaluelen(title,50)
    if titleimg != True:
        return setcors(msg=titleimg)
    brief = requestdata.get("brief")
    tags = requestdata.get("tags")
    for i in tags.split(","):
        if len(i) < 4 or len(i) > 6:
            return setcors(msg="每个标签要求不能大于6个字，不能少于4个字。")
    content = requestdata.get("content")
    valuemsg = checkvalueisNone([title,brief,tags,content])
    if valuemsg != True:
        return setcors(msg=valuemsg)
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    session = loginres[1]
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
    titleimg = checkvaluelen(title,50)
    if titleimg != True:
        return setcors(msg=titleimg)
    brief = requestdata.get("brief")
    tags = requestdata.get("tags")
    for i in tags.split(","):
        if len(i) < 4 or len(i) > 6:
            return setcors(msg="每个标签要求不能大于6个字，不能少于4个字。")
    content = requestdata.get("content")
    cid = requestdata.get("cid")
    idmsg = is_number(cid)
    if idmsg != True:
        return setcors(msg=idmsg)
    valuemsg = checkvalueisNone([title,brief,tags,content])
    if valuemsg != True:
        return setcors(msg=valuemsg)
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    session = loginres[1]
    if loginstatus is True:
        qres = db.query("select * from t_coures where status != 1 and id = {};".format(cid))
        if len(qres) != 0:
            dbres = db.commit("update t_coures set title='{}',brief='{}',tags='{}',content='{}' where id = {};".format(title,brief,tags,content,cid))
            return setcors(msg=dbres,status=200)
        else:
            return setcors(msg="修改的教程不存在")
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/couresdelete",methods=["post"])
def couresdelete():
    '''
    后台批量删除教程
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
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_coures set status = 1 where id in ({});".format(dlist))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/setcourestatus",methods=["get"])
def setcourestatus():
    '''
    后台禁用/启用教程
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    cid = request.args.get("id")
    idmsg = is_number(cid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_coures set status = (case when status = 2 then 0 else 2 end) where id = {};".format(cid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/usersfindcoures",methods=["post"])
def usersfindcoures():
    '''
    后台通过title查找教程
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    search = requestdata.get("search")
    if search == None or search == "":
        return setcors(msg="搜索内容不能为空！")
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.query("select id,title,brief,content,status,ximg,tags,author,goods,collections,follows,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_coures where status !=1 and title like '%{}%';".format(search))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)



"""
灵感管理
状态说明：0正常，1删除，2禁用
"""
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
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        inspirnum = db.query("select count(*) inspirnum  from t_inspirer where status != 1;")[0].get("inspirnum")
        res = db.query("select id,content,ximg,author,status,goods,collections,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_inspirer where status != 1 limit {},{};".format(startnum,endnum))
        data = {
            "inspirlist":res,
            "inspirnum":inspirnum
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
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_inspirer set status = 1 where id in ({});".format(dlist))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)



@adminbp.route("/setinspirstatus",methods=["get"])
def setinspirstatus():
    '''
    启用/禁用灵感
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    iid = request.args.get("id")
    idmsg = is_number(iid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_inspirer set status = (case when status = 2 then 0 else 2 end) where id = {};".format(iid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/usersfindinspirer",methods=["post"])
def usersfindinspirer():
    '''
    后台通过content或者账号，昵称查找灵感
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    search = requestdata.get("search")
    if search == None or search == "":
        return setcors(msg="搜索内容不能为空！")
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.query("select id,content,ximg,author,status,goods,collections,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_inspirer where status !=1 and content like '%{}%' or author like '%{}%';".format(search,search))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


"""
文章管理模块
"""
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
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        articlenum = db.query("select count(*) articlenum  from t_article where status != 1 ;")[0].get("articlenum")
        res = db.query("select id,title,brief,content,ximg,status,tags,author,goods,collections,follows,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_article where status != 1 limit {},{};".format(startnum,endnum))
        data = {
            "articlelist":res,
            "articlenum":articlenum
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
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_article set status = 1 where id in ({});".format(dlist))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/setarticletatus",methods=["get"])
def setarticletatus():
    '''
    启用/禁用文章
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    iid = request.args.get("id")
    idmsg = is_number(iid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_article set status = (case when status = 2 then 0 else 2 end) where id = {};".format(iid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/usersfindarticle",methods=["post"])
def usersfindarticle():
    '''
    后台通过title或者账号，昵称查找文章
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    search = requestdata.get("search")
    if search == None or search == "":
        return setcors(msg="搜索内容不能为空！")
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.query("select id,title,brief,content,ximg,status,tags,author,goods,collections,follows,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_article where status !=1 and title like '%{}%' or author like '%{}%';".format(search,search))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


"""
问题管理模块
"""
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
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        questionsnum = db.query("select count(*) questionsnum  from t_questions where status != 1 ;")[0].get("questionsnum")
        res = db.query("select id,title,brief,content,ximg,tags,author,status,goods,collections,follows,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_questions where status != 1 limit {},{};".format(startnum,endnum))
        data = {
            "questionslist":res,
            "questionsnum":questionsnum
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
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_questions set status = 1 where id in ({});".format(dlist))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/setquestiontatus",methods=["get"])
def setquestiontatus():
    '''
    启用/禁用问题
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    iid = request.args.get("id")
    idmsg = is_number(iid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_questions set status = (case when status = 2 then 0 else 2 end) where id = {};".format(iid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/usersfindquestions",methods=["post"])
def usersfindquestions():
    '''
    后台通过title或者账号，昵称查找问题
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    search = requestdata.get("search")
    if search == None or search == "":
        return setcors(msg="搜索内容不能为空！")
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.query("select id,title,brief,content,ximg,tags,author,status,goods,collections,follows,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_questions where status !=1 and title like '%{}%' or author like '%{}%';".format(search,search))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


"""
标签管理
ctype：0教程1提问2灵感3心得体会
状态0正常、1删除，2禁用
"""

@adminbp.route("/gettagslist",methods=["get"])
def gettagslist():
    '''
    后台获取标签列表
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        tid = request.args.get("id")
        if tid == "" or tid == None:
            res = db.query("select id,ctype,tags,status,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_content_tags where status != 1;")
        else:
            idmsg = is_number(tid)
            if idmsg != True:
                return setcors(msg=idmsg)
            res = db.query("select id,ctype,tags,status,DATE_FORMAT(updatetime,'%Y-%m-%d %T') updatetime from t_content_tags where status != 1 and id = {};".format(tid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)



@adminbp.route("/newtags",methods=["post"])
def newtags():
    '''
    后台新增标签列表
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    ctype = requestdata.get("ctype")
    if ctype not in (0,1,3,"0","1","3"):
        return setcors(msg="ctype只有0，1，3三种")
    tags = requestdata.get("tags")
    if tags == None or tags == "":
        return setcors(msg="tags不能为空！")
    for i in tags.split(","):
        if len(i) < 4 or len(i) > 6:
            return setcors(msg="每个标签要求不能大于6个字，不能少于4个字。")
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("insert into t_content_tags (ctype,tags) values ({},'{}');".format(ctype,tags))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/updatetags",methods=["post"])
def updatetags():
    '''
    后台修改标签列表
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    tid = requestdata.get("id")
    ctype = requestdata.get("ctype")
    if ctype not in (0,1,3,"0","1","3"):
        return setcors(msg="ctype只有0，1，3三种")
    tags = requestdata.get("tags")
    for i in tags.split(","):
        if len(i) < 4 or len(i) > 6:
            return setcors(msg="每个标签要求不能大于6个字，不能少于4个字。")
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_content_tags set ctype = '{}',tags = '{}' where id = {};".format(ctype,tags,tid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/deletetags",methods=["post"])
def deletetags():
    '''
    后台删除标签列表
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
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_content_tags set status = 1 where id in ({});".format(dlist))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/settagstatus",methods=["get"])
def settagstatus():
    '''
    启用/禁用标签
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    iid = request.args.get("id")
    idmsg = is_number(iid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.commit("update t_content_tags set status = (case when status = 2 then 0 else 2 end) where id = {};".format(iid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=loginstatus)


@adminbp.route("/gettag0list",methods=["get"])
def gettag0list():
    '''
    获取教程标签列表
    '''
    token = request.headers.get("token")
    loginres = checkadminloginstatus(token)
    loginstatus = loginres[0]
    if loginstatus is True:
        res = db.query("select tags from t_content_tags where status = 0 and ctype = 0 and uid in (0);")
        tagslist = []
        for i in range(len(res)):
            tagslist.append(res[i].get("tags"))
        tagslist = list(set(tagslist))
        res = ""
        for i in tagslist:
            res = res+i+","
        tags = {"tags":res[:-1]}
        return setcors(data=tags,status=200)
    else:
        return setcors(msg=loginstatus)