# -*- coding:utf-8 -*-
__author__ = 'LangJin'

from flask import request,render_template,session,make_response
from . import userbp
from ..utils.dbtools import Db
from config import db_config
from ..utils.othertools import checkusername,checkpasswd,create_token,setcors

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
            data["stutas"] = 401
        else:
            # password = encryption(username,password,"user")
            passwd = checkpasswd(password)
            if passwd is True:
                sql = "insert into t_user (username,password) values ('{}','{}');".format(username,password)
                msg = db.commit(sql)
                data["msg"] = "注册成功！"
                data["data"] = msg
                data["status"] = 200
            else:
                data["msg"] = "注册失败！"
                data["data"] = passwd
                data["status"] = 401
    else:
        data["msg"] = "注册失败！"
        data["data"] = usernamemsg
        data["status"] = 401

    return setcors(data)



@userbp.route("/login",methods=["post"])
def userlogin():
    '''
    用户登录接口\n
    获取json格式的数据进行处理
    '''
    data = {}
    userinfo = request.get_json()
    username = userinfo.get("username")
    password = userinfo.get("password")
    if len(username) != 0 and len(password) != 0:
        sql = "select * from t_user where username = '{}'".format(username)
        res = db.query(sql)
        
        if len(res) != 1:
            data["msg"] = "数据异常或者用户不存在！"
            data["data"] = None
            data["status"] = 401
        else:
            # password = encryption(username,password,"user")
            if password == res[0].get("password"):
                token = create_token()
                session["userinfo"] = {"token":token,"uid":res[0]["id"]}
                userinfo = {
                    "nickname":res[0]["nickname"],
                    "uid":res[0]["id"],
                    "headpic":res[0]["headpic"]
                }
                data["msg"] = "登录成功！"
                data["data"] = {}
                data["data"]["userinfo"] = userinfo
                data["data"]["token"] = token
                data["status"] = 200
            else:
                data["msg"] = "密码错误！"
                data["data"] = None
                data["status"] = 401
    else:
        data["msg"] = "账号为空"
        data["data"] = None
        data["status"] = 401
    return setcors(data)



@userbp.route("/question/new",methods=["post"])
def question():
    '''
    提问接口
    '''
    data = {}
    requestdata = request.get_json()
    token = request.headers.get("token")
    title = requestdata.get("title")
    brief = requestdata.get("brief")
    tags = requestdata.get("tags")
    content = requestdata.get("content")
    userinfo = session.get("userinfo")
    tokenid = userinfo.get("token")
    if tokenid != None and tokenid == token:
        uid = session["userinfo"]["uid"]
        dbres = db.commit("insert into t_questions (title,brief,content,tags,uid) values ('{}','{}','{}','{}',{});".format(title,brief,content,tags,uid))
        data["data"] = dbres
        data["msg"] = "提问成功"
        data["status"] = 200
    else:
        data["msg"] = "未登录"
        data["data"] = None
        data["status"] = 401
    return setcors(data)


@userbp.route("/question/update",methods=["post"])
def questionupdate():
    '''
    修改提问接口
    '''
    data = {}
    requestdata = request.get_json()
    token = request.headers.get("token")
    userinfo = session.get("userinfo")
    tokenid = userinfo.get("token")
    if tokenid != None and tokenid == token:
        title = requestdata.get("title")
        brief = requestdata.get("brief")
        tags = requestdata.get("tags")
        content = requestdata.get("content")
        qid = requestdata.get("qid")
        uid = session["userinfo"]["uid"]
        qres = db.query("select * from t_questions where uid ={} and status = 0;".format(uid))
        qlist = []
        if len(qres) != 0:
            for i in qres:
                qlist.append(i["id"])
            if qid in qlist:
                dbres = db.commit("update t_questions set title='{}',brief='{}',tags='{}',content='{}' where id = {} and uid = {};".format(title,brief,tags,content,qid,uid))
                data["status"] = 200
                data["msg"] = "修改成功"
                data["data"] = dbres
            else:
                data["status"] = 401
                data["msg"] = "内容不存在"
                data["data"] = None
        else:
            data["status"] = 401
            data["msg"] = "内容不存在"
            data["data"] = None
    else:
        data["status"] = 401
        data["msg"] = "未登录"
        data["data"] = None
    return setcors(data)

@userbp.route("/question/delete",methods=["post"])
def questiondelete():
    '''
    删除提问接口
    '''
    data = {}
    requestdata = request.get_json()
    token = request.headers.get("token")
    qid = requestdata.get("qid")
    userinfo = session.get("userinfo")
    tokenid = userinfo.get("token")
    if tokenid != None and tokenid == token:
        uid = session["userinfo"]["uid"]
        qres = db.query("select * from t_questions where uid ={} and status = 0;".format(uid))
        qlist = []
        if len(qres) != 0:
            for i in qres:
                qlist.append(i["id"])
            if qid in qlist:
                dbres = db.commit("update t_questions set status = 1 where id = {} and uid = {};".format(qid,uid))
                data["status"] = 200
                data["msg"] = "删除成功"
                data["data"] = dbres
            else:
                data["status"] = 401
                data["msg"] = "内容不存在"
                data["data"] = None
        else:
            data["status"] = 401
            data["msg"] = "内容不存在"
            data["data"] = None
    else:
        data["status"] = 401
        data["msg"] = "未登录"
        data["data"] = None
    return setcors(data)


@userbp.route("/inspirer/new",methods=["post"])
def inspirer():
    '''
    发表灵感
    '''
    data = {}
    requestdata = request.get_json()
    token = request.headers.get("token")
    content = requestdata.get("content")
    userinfo = session.get("userinfo")
    tokenid = userinfo.get("token")
    if tokenid != None and tokenid == token:
        uid = session["userinfo"]["uid"]
        dbres = db.commit("insert into t_inspirer (content,uid) values ('{}',{});".format(content,uid))
        data["data"] = dbres
        data["msg"] = "提问成功"
        data["status"] = 200
    else:
        data["msg"] = "未登录"
        data["data"] = None
        data["status"] = 401
    return setcors(data)


@userbp.route("/inspirer/update",methods=["post"])
def inspirerupdate():
    '''
    修改灵感
    '''
    data = {}
    questiondata = request.get_json()
    token = request.headers.get("token")
    userinfo = session.get("userinfo")
    tokenid = userinfo.get("token")
    if tokenid != None and tokenid == token:
        content = questiondata.get("content")
        if content != None and content != "":
            iid = questiondata.get("iid")
            uid = session["userinfo"]["uid"]
            dbres = db.commit("update t_inspirer set content = '{}' where id = {} ;".format(content,iid))
            data["data"] = dbres
            data["msg"] = "修改成功"
            data["status"] = 200
        else:
            data["data"] = None
            data["msg"] = "修改内容不能为空！"
            data["status"] = 200
    else:
        data["msg"] = "未登录"
        data["data"] = None
        data["status"] = 401
    return setcors(data)


@userbp.route("/inspirer/delete",methods=["post"])
def inspirerdelete():
    '''
    删除灵感
    '''
    data = {}
    questiondata = request.get_json()
    token = request.headers.get("token")
    iid = questiondata.get("iid")
    userinfo = session.get("userinfo")
    tokenid = userinfo.get("token")
    if tokenid != None and tokenid == token:
        uid = session["userinfo"]["uid"]
        dbres = db.commit("update t_inspirer set status = 1 where id = {} ;".format(iid))
        data["data"] = dbres
        data["msg"] = "删除成功"
        data["status"] = 200
    else:
        data["msg"] = "未登录"
        data["data"] = None
        data["status"] = 401
    return setcors(data)


@userbp.route("/article/new",methods=["post"])
def article():
    '''
    写文章接口
    '''
    data = {}
    requestdata = request.get_json()
    token = request.headers.get("token")
    title = requestdata.get("title")
    tags = requestdata.get("tags")
    content = requestdata.get("content")
    brief = requestdata.get("brief")
    userinfo = session.get("userinfo")
    tokenid = userinfo.get("token")
    if tokenid != None and tokenid == token:
        uid = session["userinfo"]["uid"]
        dbres = db.commit("insert into t_article (title,brief,content,tags,uid) values ('{}','{}','{}','{}',{});".format(title,brief,content,tags,uid))
        data["data"] = dbres
        data["msg"] = "发表成功"
        data["status"] = 200
    else:
        data["msg"] = "未登录"
        data["data"] = None
        data["status"] = 401
    return setcors(data)


@userbp.route("/article/update",methods=["post"])
def articleupdate():
    '''
    修改文章接口
    '''
    data = {}
    requestdata = request.get_json()
    token = request.headers.get("token")
    title = requestdata.get("title")
    tags = requestdata.get("tags")
    content = requestdata.get("content")
    author = requestdata.get("nickname")
    aid = requestdata.get("aid")
    userinfo = session.get("userinfo")
    tokenid = userinfo.get("token")
    if tokenid != None and tokenid == token:
        uid = session["userinfo"]["uid"]
        dbres = db.commit("update t_article set title='{}',tags='{}',content='{}' where id ={};".format(title,tags,content,aid))
        data["data"] = dbres
        data["msg"] = "修改成功"
        data["status"] = 200
    else:
        data["msg"] = "未登录"
        data["data"] = None
        data["status"] = 401
    return setcors(data)

@userbp.route("/article/delete",methods=["post"])
def articledelete():
    '''
    删除文章接口
    '''
    data = {}
    requestdata = request.get_json()
    token = request.headers.get("token")
    aid = requestdata.get("aid")
    userinfo = session.get("userinfo")
    tokenid = userinfo.get("token")
    if tokenid != None and tokenid == token:
        uid = session["userinfo"]["uid"]
        dbres = db.commit("update t_article set status=1 where id ={} and uid = {};".format(aid,uid))
        data["data"] = dbres
        data["msg"] = "删除成功"
        data["status"] = 200
    else:
        data["msg"] = "未登录"
        data["data"] = None
        data["status"] = 401
    return setcors(data)

@userbp.route("/updateuserinfo",methods=["post"])
def updateuserinfo():
    '''
    修改个人资料接口
    '''
    data = {}
    requestdata = request.get_json()
    token = request.headers.get("token")
    nickname = requestdata.get("nickname")
    titlepic = requestdata.get("titlepic")
    headpic = requestdata.get("headpic")
    phone = requestdata.get("phone")
    sex = requestdata.get("sex")
    job = requestdata.get("job")
    email = requestdata.get("email")
    weixin = requestdata.get("weixin")
    qq = requestdata.get("qq")
    qianming = requestdata.get("userinfo")
    address = requestdata.get("address")
    userinfo = session.get("userinfo")
    tokenid = userinfo.get("token")
    if tokenid != None and tokenid == token:  
        uid = userinfo.get("uid")
        dbres = db.commit("update t_user set nickname='{}', titlepic='{}', headpic='{}', phone='{}', sex='{}', job='{}', email='{}',\
        weixin ='{}', QQ='{}', userinfo='{}', address='{}' where id={};".format(nickname,titlepic,headpic,phone,sex,job,email,weixin,qq,qianming,address,uid))
        data["data"] = dbres
        data["msg"] = "修改成功"
        data["status"] = 200    
    else:
        data["msg"] = "未登录"
        data["data"] = None
        data["status"] = 401
    return setcors(data)


@userbp.route("/userfellgoods",methods=["post"])
def userfellgoods():
    '''
    点赞
    '''
    data = {}
    token = request.headers.get("token")
    userinfo = session.get("userinfo")
    tokenid = userinfo.get("token")
    if tokenid != None and tokenid == token:
        uid = session["userinfo"]["uid"]
        requestdata = request.get_json()
        # {"goodtype":"article","status":0,"gid":1}
        goodtype = requestdata.get("goodtype")
        status = requestdata.get("status")
        gid = requestdata.get("gid")
        if goodtype == "article":
            qres = db.query("select * from t_article_user_status where uid = {} and aid = {};".format(uid,gid))
            goods = db.query("select goods from t_article where id = {}".format(gid))[0]["goods"]
            if len(qres) == 0  and status == 0:  #没有点赞的情况下点赞
                goods = goods + 1
                dzres = db.commit("insert into t_article_user_status (aid,uid,gstatus) values ({},{},0);".format(gid,uid))
                upres = db.commit("update t_article set goods={} where id ={};".format(goods,gid))
                data["data"] = (dzres,upres)
                data["msg"] = "点赞成功！"
                data["status"] = 200
            elif len(qres) == 0  and status == 1: #没有点赞的情况下取消点赞
                data["data"] = None
                data["msg"] = "你还没有对该文章点赞过！"
                data["status"] = 401        
            elif len(qres) == 1  and status == 0:  #有点赞的情况下点赞:
                data["data"] = None
                data["msg"] = "你已经点赞过！"
                data["status"] = 401     
            else:
                goods = goods - 1
                dzres = db.commit("update t_article_user_status set gstatus = 1 where  uid = {} and aid = {};".format(uid,gid))
                upres = db.commit("update t_article set goods={} where id ={};".format(goods,gid))
                data["data"] = (dzres,upres)
                data["msg"] = "取消点赞成功！"
                data["status"] = 200
        elif goodtype == "coures":
            qres = db.query("select * from t_coures_user_status where uid = {} and aid = {};".format(uid,gid))
            goods = db.query("select goods from t_coures where id = {}".format(gid))[0]["goods"]
            if len(qres) == 0  and status == 0:  #没有点赞的情况下点赞
                goods = goods + 1
                dzres = db.commit("insert into t_coures_user_status (aid,uid,gstatus) values ({},{},0);".format(gid,uid))
                upres = db.commit("update t_coures set goods={} where id ={};".format(goods,gid))
                data["data"] = (dzres,upres)
                data["msg"] = "点赞成功！"
                data["status"] = 200
            elif len(qres) == 0  and status == 1: #没有点赞的情况下取消点赞
                data["data"] = None
                data["msg"] = "你还没有对该文章点赞过！"
                data["status"] = 401        
            elif len(qres) == 1  and status == 0:  #有点赞的情况下点赞:
                data["data"] = None
                data["msg"] = "你已经点赞过！"
                data["status"] = 401     
            else:
                goods = goods - 1
                dzres = db.commit("update t_coures_user_status set gstatus = 1 where  uid = {} and aid = {};".format(uid,gid))
                upres = db.commit("update t_coures set goods={} where id ={};".format(goods,gid))
                data["data"] = (dzres,upres)
                data["msg"] = "取消点赞成功！"
                data["status"] = 200
        elif goodtype == "inspirer":
            qres = db.query("select * from t_inspirer_user_status where uid = {} and aid = {};".format(uid,gid))
            goods = db.query("select goods from t_inspirer where id = {}".format(gid))[0]["goods"]
            if len(qres) == 0  and status == 0:  #没有点赞的情况下点赞
                goods = goods + 1
                dzres = db.commit("insert into t_inspirer_user_status (aid,uid,gstatus) values ({},{},0);".format(gid,uid))
                upres = db.commit("update t_inspirer set goods={} where id ={};".format(goods,gid))
                data["data"] = (dzres,upres)
                data["msg"] = "点赞成功！"
                data["status"] = 200
            elif len(qres) == 0  and status == 1: #没有点赞的情况下取消点赞
                data["data"] = None
                data["msg"] = "你还没有对该文章点赞过！"
                data["status"] = 401        
            elif len(qres) == 1  and status == 0:  #有点赞的情况下点赞:
                data["data"] = None
                data["msg"] = "你已经点赞过！"
                data["status"] = 401     
            else:
                goods = goods - 1
                dzres = db.commit("update t_inspirer_user_status set gstatus = 1 where  uid = {} and aid = {};".format(uid,gid))
                upres = db.commit("update t_inspirer set goods={} where id ={};".format(goods,gid))
                data["data"] = (dzres,upres)
                data["msg"] = "取消点赞成功！"
                data["status"] = 200
        elif goodtype == "questions":
            qres = db.query("select * from t_questions_user_status where uid = {} and aid = {};".format(uid,gid))
            goods = db.query("select goods from t_questions where id = {}".format(gid))[0]["goods"]
            if len(qres) == 0  and status == 0:  #没有点赞的情况下点赞
                goods = goods + 1
                dzres = db.commit("insert into questions_user_status (aid,uid,gstatus) values ({},{},0);".format(gid,uid))
                upres = db.commit("update t_questions set goods={} where id ={};".format(goods,gid))
                data["data"] = (dzres,upres)
                data["msg"] = "点赞成功！"
                data["status"] = 200
            elif len(qres) == 0  and status == 1: #没有点赞的情况下取消点赞
                data["data"] = None
                data["msg"] = "你还没有对该文章点赞过！"
                data["status"] = 401        
            elif len(qres) == 1  and status == 0:  #有点赞的情况下点赞:
                data["data"] = None
                data["msg"] = "你已经点赞过！"
                data["status"] = 401     
            else:
                goods = goods - 1
                dzres = db.commit("update t_questions_user_status set gstatus = 1 where  uid = {} and aid = {};".format(uid,gid))
                upres = db.commit("update t_questions set goods={} where id ={};".format(goods,gid))
                data["data"] = (dzres,upres)
                data["msg"] = "取消点赞成功！"
                data["status"] = 200
        else:
            data["data"] = None
            data["msg"] = "不存在该文章类型"
            data["status"] = 401
    else:
        data["msg"] = "未登录"
        data["data"] = None
        data["status"] = 401
    return setcors(data)




@userbp.route("/test")
def test():
    headers  = request.args.get("token")
    data = {}
    data["msg"] = "测试接口"
    data["data"] = headers
    data["stutas"] = 200
    return setcors(data)