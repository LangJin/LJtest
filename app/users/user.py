# -*- coding:utf-8 -*-
__author__ = 'LangJin'

from flask import request,render_template,session,make_response
from . import userbp
from ..utils.dbtools import Db
from config import db_config
from ..utils.othertools import checkusername,checkpasswd,create_token,setcors,checkloginstatus,checkContentType

db = Db(db_config)


@userbp.route("/regist",methods=["post"])
def regist():
    '''
    用户注册接口\n
    获取json格式的数据进行处理
    '''
    data = {}
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        data["msg"] = "请求失败！"
        data["data"] = headrsmsg
        data["status"] = 401
        return setcors(data)
    userinfo = request.get_json()
    username = userinfo.get("username")
    password = userinfo.get("password")
    usernamemsg = checkusername(username)
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
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        data["msg"] = "请求失败！"
        data["data"] = headrsmsg
        data["status"] = 401
        return setcors(data)
    userinfo = request.get_json()
    username = userinfo.get("username")
    password = userinfo.get("password")
    if password == "" or password == None:
        data["msg"] = "密码不能为空"
        data["data"] = None
        data["status"] = 401
        return setcors(data)
    if username == "" or username == None:
        data["msg"] = "账号不能为空"
        data["data"] = None
        data["status"] = 401
        return setcors(data)
    if len(username) != 0 and len(password) != 0:
        sql = "select * from t_user where status = 0 and username = '{}'".format(username)
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
                print(session)
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
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        data["msg"] = "请求失败！"
        data["data"] = headrsmsg
        data["status"] = 401
        return setcors(data)
    requestdata = request.get_json()
    token = request.headers.get("token")
    title = requestdata.get("title")
    brief = requestdata.get("brief")
    tags = requestdata.get("tags")
    content = requestdata.get("content")
    if checkloginstatus(session,token) is True:
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
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        data["msg"] = "请求失败！"
        data["data"] = headrsmsg
        data["status"] = 401
        return setcors(data)
    requestdata = request.get_json()
    token = request.headers.get("token")
    if checkloginstatus(session,token) is True:
        title = requestdata.get("title")
        brief = requestdata.get("brief")
        tags = requestdata.get("tags")
        content = requestdata.get("content")
        qid = requestdata.get("qid")
        if qid == None or qid == "":
            data["msg"] = "qid不能为空"
            data["data"] = None
            data["status"] = 401
            return setcors(data)
        uid = session["userinfo"]["uid"]
        qres = db.query("select * from t_questions where uid ={} and status = 0 and id = {};".format(uid,qid))
        if len(qres) != 0:
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
        data["msg"] = "未登录"
        data["data"] = None
    return setcors(data)


@userbp.route("/question/delete",methods=["post"])
def questiondelete():
    '''
    删除提问接口
    '''
    data = {}
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        data["msg"] = "请求失败！"
        data["data"] = headrsmsg
        data["status"] = 401
        return setcors(data)
    requestdata = request.get_json()
    token = request.headers.get("token")
    qid = requestdata.get("qid")
    if qid == None or qid == "":
        data["msg"] = "qid不能为空"
        data["data"] = None
        data["status"] = 401
        return setcors(data)
    if checkloginstatus(session,token) is True:
        uid = session["userinfo"]["uid"]
        qres = db.query("select * from t_questions where uid ={} and status = 0 and id = {};".format(uid,qid))
        if len(qres) != 0:
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
        data["msg"] = "未登录"
        data["data"] = None
    return setcors(data)


@userbp.route("/inspirer/new",methods=["post"])
def inspirer():
    '''
    发表灵感
    '''
    data = {}
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        data["msg"] = "请求失败！"
        data["data"] = headrsmsg
        data["status"] = 401
        return setcors(data)
    requestdata = request.get_json()
    token = request.headers.get("token")
    content = requestdata.get("content")
    if checkloginstatus(session,token) is True:
        if content != None or content != "":
            uid = session["userinfo"]["uid"]
            dbres = db.commit("insert into t_inspirer (content,uid) values ('{}',{});".format(content,uid))
            data["data"] = dbres
            data["msg"] = "发表成功"
            data["status"] = 200
        else:
            data["msg"] = "内容不能为空"
            data["data"] = None
            data["status"] = 401
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
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        data["msg"] = "请求失败！"
        data["data"] = headrsmsg
        data["status"] = 401
        return setcors(data)
    questiondata = request.get_json()
    token = request.headers.get("token")
    if checkloginstatus(session,token) is True:
        content = questiondata.get("content")
        if content != None and content != "":
            iid = questiondata.get("iid")
            if iid == None or iid == "":
                data["msg"] = "qid不能为空"
                data["data"] = None
                data["status"] = 401
                return setcors(data)
            uid = session["userinfo"]["uid"]
            qres = db.query("select * from t_inspirer where uid ={} and status = 0 and id = {};".format(uid,iid))
            if len(qres) != 0:
                dbres = db.commit("update t_inspirer set content = '{}' where id = {} ;".format(content,iid))
                data["data"] = dbres
                data["msg"] = "修改成功"
                data["status"] = 200
            else:
                data["data"] = None
                data["msg"] = "修改的内容不存在"
                data["status"] = 401 
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
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        data["msg"] = "请求失败！"
        data["data"] = headrsmsg
        data["status"] = 401
        return setcors(data)
    questiondata = request.get_json()
    token = request.headers.get("token")
    iid = questiondata.get("iid")
    if iid == None or iid == "":
        data["msg"] = "qid不能为空"
        data["data"] = None
        data["status"] = 401
        return setcors(data)
    if checkloginstatus(session,token) is True:
        uid = session["userinfo"]["uid"]
        ires = db.query("select * from t_inspirer from uid = {} and status = 0 and id = {}".format(uid,iid))
        if len(ires) != 0:
            dbres = db.commit("update t_inspirer set status = 1 where id = {} ;".format(iid))
            data["data"] = dbres
            data["msg"] = "删除成功"
            data["status"] = 200
        else:
            data["data"] = None
            data["msg"] = "内容不存在"
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
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        data["msg"] = "请求失败！"
        data["data"] = headrsmsg
        data["status"] = 401
        return setcors(data)
    requestdata = request.get_json()
    token = request.headers.get("token")
    title = requestdata.get("title")
    tags = requestdata.get("tags")
    content = requestdata.get("content")
    brief = requestdata.get("brief")
    if checkloginstatus(session,token) is True:
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
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        data["msg"] = "请求失败！"
        data["data"] = headrsmsg
        data["status"] = 401
        return setcors(data)
    requestdata = request.get_json()
    token = request.headers.get("token")
    title = requestdata.get("title")
    tags = requestdata.get("tags")
    content = requestdata.get("content")
    author = requestdata.get("nickname")
    aid = requestdata.get("aid")
    if aid == None or aid == "":
        data["msg"] = "qid不能为空"
        data["data"] = None
        data["status"] = 401
        return setcors(data)
    if checkloginstatus(session,token) is True:
        uid = session["userinfo"]["uid"]
        ares = db.query("select * from t_article where status =0 and uid ={} and id = {};".format(uid,aid))
        if len(ares) != 0: 
            dbres = db.commit("update t_article set title='{}',tags='{}',content='{}' where id ={};".format(title,tags,content,aid))
            data["data"] = dbres
            data["msg"] = "修改成功"
            data["status"] = 200
        else:
            data["data"] = None
            data["msg"] = "内容不存在"
            data["status"] = 401        
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
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        data["msg"] = "请求失败！"
        data["data"] = headrsmsg
        data["status"] = 401
        return setcors(data)
    requestdata = request.get_json()
    token = request.headers.get("token")
    aid = requestdata.get("aid")
    if aid == None or aid == "":
        data["msg"] = "qid不能为空"
        data["data"] = None
        data["status"] = 401
        return setcors(data)
    if checkloginstatus(session,token) is True:
        uid = session["userinfo"]["uid"]
        ares = db.query("select * from t_article where status =0 and uid ={} and id = {};".format(uid,aid))
        if len(ares) != 0: 
            dbres = db.commit("update t_article set status=1 where id ={} and uid = {};".format(aid,uid))
            data["data"] = dbres
            data["msg"] = "删除成功"
            data["status"] = 200
        else:
            data["data"] = None
            data["msg"] = "内容不存在"
            data["status"] = 401  
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
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        data["msg"] = "请求失败！"
        data["data"] = headrsmsg
        data["status"] = 401
        return setcors(data)
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
    if checkloginstatus(session,token) is True:
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
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        data["msg"] = "请求失败！"
        data["data"] = headrsmsg
        data["status"] = 401
        return setcors(data)
    token = request.headers.get("token")
    if checkloginstatus(session,token) is True:
        uid = session["userinfo"]["uid"]
        requestdata = request.get_json()
        # {"goodtype":"article","status":0,"gid":1}
        goodtype = requestdata.get("goodtype")
        status = requestdata.get("status")
        gid = requestdata.get("gid")
        if gid == None or gid == "":
            data["data"] = None
            data["msg"] = "cid不能为空！！"
            data["status"] = 401  
            return setcors(data)
        if status in [0,1]:
            if goodtype == "article":
                qres = db.query("select * from t_article_user_status where uid = {} and aid = {};".format(uid,gid))
                goods = db.query("select goods from t_article where id = {} and status = 0;".format(gid))
                if len(goods) != 0 :
                    goods = goods[0]["goods"]
                    if len(qres) == 0:  # 从来没有点过赞
                        if status == 0: # 点赞
                            goods = goods + 1
                            dzres = db.commit("insert into t_article_user_status (aid,uid,gstatus) values ({},{},0);".format(gid,uid))
                            upres = db.commit("update t_article set goods={} where id ={};".format(goods,gid))
                            data["data"] = (dzres,upres)
                            data["msg"] = "点赞成功！"
                            data["status"] = 200
                        else:  #取消点赞
                            data["data"] = None
                            data["msg"] = "你还没有对该文章点赞过！"
                            data["status"] = 401  
                    else:
                        gstatus = db.query("select gstatus from t_article_user_status where aid = {} and uid = {};".format(gid,uid))[0]["gstatus"]
                        if status == 0: # 点赞
                            if gstatus == 0:
                                data["data"] = None
                                data["msg"] = "已经点过赞了"
                                data["status"] = 401                         
                            else:
                                goods = goods + 1
                                dzres = db.commit("update t_article_user_status set gstatus = 0 where  uid = {} and aid = {};".format(uid,gid))
                                upres = db.commit("update t_article set goods={} where id ={};".format(goods,gid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "点赞成功！"
                                data["status"] = 200   
                        else: # 取消点赞
                            if gstatus == 0:
                                goods = goods - 1
                                dzres = db.commit("update t_article_user_status set gstatus = 1 where  uid = {} and aid = {};".format(uid,gid))
                                upres = db.commit("update t_article set goods={} where id ={};".format(goods,gid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "取消点赞成功！"
                                data["status"] = 200
                            else:
                                data["data"] = None
                                data["msg"] = "你还没有对该文章点赞过！"
                                data["status"] = 401  
                else:
                    data["data"] = None
                    data["msg"] = "不存在该文章"
                    data["status"] = 401               
            elif goodtype == "coures":
                qres = db.query("select * from t_coures_user_status where uid = {} and cid = {};".format(uid,gid))
                goods = db.query("select goods from t_coures where id = {} and status = 0;".format(gid))
                if len(goods) != 0 :
                    goods = goods[0]["goods"]
                    if len(qres) == 0:  # 从来没有点过赞
                        if status == 0: # 点赞
                            goods = goods + 1
                            dzres = db.commit("insert into t_coures_user_status (cid,uid,gstatus) values ({},{},0);".format(gid,uid))
                            upres = db.commit("update t_coures set goods={} where id ={};".format(goods,gid))
                            data["data"] = (dzres,upres)
                            data["msg"] = "点赞成功！"
                            data["status"] = 200
                        else:  #取消点赞
                            data["data"] = None
                            data["msg"] = "你还没有对该文章点赞过！"
                            data["status"] = 401  
                    else:
                        gstatus = db.query("select gstatus from t_coures_user_status where cid = {} and uid = {};".format(gid,uid))[0]["gstatus"]
                        if status == 0: # 点赞
                            if gstatus == 0:
                                data["data"] = None
                                data["msg"] = "已经点过赞了"
                                data["status"] = 401                         
                            else:
                                goods = goods + 1
                                dzres = db.commit("update t_coures_user_status set gstatus = 0 where  uid = {} and cid = {};".format(uid,gid))
                                upres = db.commit("update t_coures set goods={} where id ={};".format(goods,gid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "点赞成功！"
                                data["status"] = 200   
                        else: # 取消点赞
                            if gstatus == 0:
                                goods = goods - 1
                                dzres = db.commit("update t_coures_user_status set gstatus = 1 where  uid = {} and cid = {};".format(uid,gid))
                                upres = db.commit("update t_coures set goods={} where id ={};".format(goods,gid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "取消点赞成功！"
                                data["status"] = 200
                            else:
                                data["data"] = None
                                data["msg"] = "你还没有对该文章点赞过！"
                                data["status"] = 401      
                else:
                    data["data"] = None
                    data["msg"] = "不存在该文章"
                    data["status"] = 401    
            elif goodtype == "inspirer":
                qres = db.query("select * from t_inspirer_user_status where uid = {} and iid = {};".format(uid,gid))
                goods = db.query("select goods from t_inspirer where id = {} and status = 0;".format(gid))
                if len(goods) != 0 :
                    goods = goods[0]["goods"]
                    if len(qres) == 0:  # 从来没有点过赞
                        if status == 0: # 点赞
                            goods = goods + 1
                            dzres = db.commit("insert into t_inspirer_user_status (iid,uid,gstatus) values ({},{},0);".format(gid,uid))
                            upres = db.commit("update t_inspirer set goods={} where id ={};".format(goods,gid))
                            data["data"] = (dzres,upres)
                            data["msg"] = "点赞成功！"
                            data["status"] = 200
                        else:  #取消点赞
                            data["data"] = None
                            data["msg"] = "你还没有对该文章点赞过！"
                            data["status"] = 401  
                    else:
                        gstatus = db.query("select gstatus from t_inspirer_user_status where iid = {} and uid = {}".format(gid,uid))[0]["gstatus"]
                        if status == 0: # 点赞
                            if gstatus == 0:
                                data["data"] = None
                                data["msg"] = "已经点过赞了"
                                data["status"] = 401                         
                            else:
                                goods = goods + 1
                                dzres = db.commit("update t_inspirer_user_status set gstatus = 0 where  uid = {} and iid = {};".format(uid,gid))
                                upres = db.commit("update t_inspirer set goods={} where id ={};".format(goods,gid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "点赞成功！"
                                data["status"] = 200   
                        else: # 取消点赞
                            if gstatus == 0:
                                goods = goods - 1
                                dzres = db.commit("update t_inspirer_user_status set gstatus = 1 where  uid = {} and iid = {};".format(uid,gid))
                                upres = db.commit("update t_inspirer set goods={} where id ={};".format(goods,gid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "取消点赞成功！"
                                data["status"] = 200
                            else:
                                data["data"] = None
                                data["msg"] = "你还没有对该文章点赞过！"
                                data["status"] = 401   
                else:
                    data["data"] = None
                    data["msg"] = "不存在该文章"
                    data["status"] = 401    
            elif goodtype == "questions":
                qres = db.query("select * from t_questions_user_status where uid = {} and qid = {};".format(uid,gid))
                goods = db.query("select goods from t_questions where id = {} and status = 0;".format(gid))
                if len(goods) != 0 :
                    goods = goods[0]["goods"]
                    if len(qres) == 0:  # 从来没有点过赞
                        if status == 0: # 点赞
                            goods = goods + 1
                            dzres = db.commit("insert into t_questions_user_status (qid,uid,gstatus) values ({},{},0);".format(gid,uid))
                            upres = db.commit("update t_questions set goods={} where id ={};".format(goods,gid))
                            data["data"] = (dzres,upres)
                            data["msg"] = "点赞成功！"
                            data["status"] = 200
                        else:  #取消点赞
                            data["data"] = None
                            data["msg"] = "你还没有对该文章点赞过！"
                            data["status"] = 401  
                    else:
                        gstatus = db.query("select gstatus from t_questions_user_status where qid = {} and uid = {};".format(gid,uid))[0]["gstatus"]
                        if status == 0: # 点赞
                            if gstatus == 0:
                                data["data"] = None
                                data["msg"] = "已经点过赞了"
                                data["status"] = 401                         
                            else:
                                goods = goods + 1
                                dzres = db.commit("update t_questions_user_status set gstatus = 0 where  uid = {} and qid = {};".format(uid,gid))
                                upres = db.commit("update t_questions set goods={} where id ={};".format(goods,gid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "点赞成功！"
                                data["status"] = 200   
                        else: # 取消点赞
                            if gstatus == 0:
                                goods = goods - 1
                                dzres = db.commit("update t_questions_user_status set gstatus = 1 where  uid = {} and qid = {};".format(uid,gid))
                                upres = db.commit("update t_questions set goods={} where id ={};".format(goods,gid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "取消点赞成功！"
                                data["status"] = 200
                            else:
                                data["data"] = None
                                data["msg"] = "你还没有对该文章点赞过！"
                                data["status"] = 401   
                else:
                    data["data"] = None
                    data["msg"] = "不存在该文章"
                    data["status"] = 401    
            else:
                data["data"] = None
                data["msg"] = "不存在该文章类型"
                data["status"] = 401
        else:
            data["msg"] = "状态不正确，仅0或者1"
            data["data"] = None
            data["status"] = 401 
    else:
        data["msg"] = "未登录"
        data["data"] = None
        data["status"] = 401
    return setcors(data)



@userbp.route("/usercollections",methods=["post"])
def usercollections():
    '''
    收藏
    '''
    data = {}
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        data["msg"] = "请求失败！"
        data["data"] = headrsmsg
        data["status"] = 401
        return setcors(data)
    token = request.headers.get("token")
    if checkloginstatus(session,token) is True:
        uid = session["userinfo"]["uid"]
        requestdata = request.get_json()
        # {"collectiontype":"article","status":0,"cid":1}
        collectiontype = requestdata.get("collectiontype")
        status = requestdata.get("status")
        cid = requestdata.get("cid")
        if cid == None or cid == "":
            data["data"] = None
            data["msg"] = "cid不能为空！！"
            data["status"] = 401  
            return setcors(data)
        if status in [0,1]:
            if collectiontype == "article":
                qres = db.query("select * from t_article_user_status where uid = {} and aid = {};".format(uid,cid))
                collections = db.query("select collections from t_article where id = {}  and status = 0;".format(cid))
                if len(collections) != 0 :
                    collections = collections[0]["collections"]
                    if len(qres) == 0:  # 从来没有点过赞
                        if status == 0: # 点赞
                            collections = collections + 1
                            dzres = db.commit("insert into t_article_user_status (aid,uid,cstatus) values ({},{},0);".format(cid,uid))
                            upres = db.commit("update t_article set collections={} where id ={};".format(collections,cid))
                            data["data"] = (dzres,upres)
                            data["msg"] = "收藏成功！"
                            data["status"] = 200
                        else:  #取消点赞
                            data["data"] = None
                            data["msg"] = "你还没有对该文章收藏过！"
                            data["status"] = 401  
                    else:
                        cstatus = db.query("select cstatus from t_article_user_status where aid = {} and uid = {};".format(cid,uid))[0]["cstatus"]
                        if status == 0: # 点赞
                            if cstatus == 0:
                                data["data"] = None
                                data["msg"] = "已经收藏过了"
                                data["status"] = 401                         
                            else:
                                collections = collections + 1
                                dzres = db.commit("update t_article_user_status set cstatus = 0 where  uid = {} and aid = {};".format(uid,cid))
                                upres = db.commit("update t_article set collections={} where id ={};".format(collections,cid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "收藏成功！"
                                data["status"] = 200   
                        else: # 取消点赞
                            if cstatus == 0:
                                collections = collections - 1
                                dzres = db.commit("update t_article_user_status set cstatus = 1 where  uid = {} and aid = {};".format(uid,cid))
                                upres = db.commit("update t_article set collections={} where id ={};".format(collections,cid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "取消收藏成功！"
                                data["status"] = 200
                            else:
                                data["data"] = None
                                data["msg"] = "你还没有对该文章收藏过！"
                                data["status"] = 401  
                else:
                    data["data"] = None
                    data["msg"] = "不存在该文章"
                    data["status"] = 401               
            elif collectiontype == "coures":
                qres = db.query("select * from t_coures_user_status where uid = {} and cid = {};".format(uid,cid))
                collections = db.query("select collections from t_coures where id = {} and status = 0;".format(cid))
                if len(collections) != 0 :
                    collections = collections[0]["collections"]
                    if len(qres) == 0:  # 从来没有点过赞
                        if status == 0: # 点赞
                            collections = collections + 1
                            dzres = db.commit("insert into t_coures_user_status (cid,uid,cstatus) values ({},{},0);".format(cid,uid))
                            upres = db.commit("update t_coures set collections={} where id ={};".format(collections,cid))
                            data["data"] = (dzres,upres)
                            data["msg"] = "收藏成功！"
                            data["status"] = 200
                        else:  #取消点赞
                            data["data"] = None
                            data["msg"] = "你还没有对该文章收藏过！"
                            data["status"] = 401  
                    else:
                        cstatus = db.query("select cstatus from t_coures_user_status where cid = {} and uid = {};".format(cid,uid))[0]["cstatus"]
                        if status == 0: # 点赞
                            if cstatus == 0:
                                data["data"] = None
                                data["msg"] = "已经收藏过了"
                                data["status"] = 401                         
                            else:
                                collections = collections + 1
                                dzres = db.commit("update t_coures_user_status set cstatus = 0 where  uid = {} and cid = {};".format(uid,cid))
                                upres = db.commit("update t_coures set collections={} where id ={};".format(collections,cid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "收藏成功！"
                                data["status"] = 200   
                        else: # 取消点赞
                            if cstatus == 0:
                                collections = collections - 1
                                dzres = db.commit("update t_coures_user_status set cstatus = 1 where  uid = {} and cid = {};".format(uid,cid))
                                upres = db.commit("update t_coures set collections={} where id ={};".format(collections,cid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "取消收藏成功！"
                                data["status"] = 200
                            else:
                                data["data"] = None
                                data["msg"] = "你还没有对该文章收藏过！"
                                data["status"] = 401      
                else:
                    data["data"] = None
                    data["msg"] = "不存在该文章"
                    data["status"] = 401    
            elif collectiontype == "inspirer":
                qres = db.query("select * from t_inspirer_user_status where uid = {} and iid = {};".format(uid,cid))
                collections = db.query("select collections from t_inspirer where id = {} and status = 0;".format(cid))
                if len(collections) != 0 :
                    collections = collections[0]["collections"]
                    if len(qres) == 0:  # 从来没有点过赞
                        if status == 0: # 点赞
                            collections = collections + 1
                            dzres = db.commit("insert into t_inspirer_user_status (iid,uid,cstatus) values ({},{},0);".format(cid,uid))
                            upres = db.commit("update t_inspirer set collections={} where id ={};".format(collections,cid))
                            data["data"] = (dzres,upres)
                            data["msg"] = "收藏成功！"
                            data["status"] = 200
                        else:  #取消点赞
                            data["data"] = None
                            data["msg"] = "你还没有对该文章收藏过！"
                            data["status"] = 401  
                    else:
                        cstatus = db.query("select cstatus from t_inspirer_user_status where iid = {} and uid = {};".format(cid,uid))[0]["cstatus"]
                        if status == 0: # 点赞
                            if cstatus == 0:
                                data["data"] = None
                                data["msg"] = "已经收藏过了"
                                data["status"] = 401                         
                            else:
                                collections = collections + 1
                                dzres = db.commit("update t_inspirer_user_status set cstatus = 0 where  uid = {} and iid = {};".format(uid,cid))
                                upres = db.commit("update t_inspirer set collections={} where id ={};".format(collections,cid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "收藏成功！"
                                data["status"] = 200   
                        else: # 取消点赞
                            if cstatus == 0:
                                collections = collections - 1
                                dzres = db.commit("update t_inspirer_user_status set cstatus = 1 where  uid = {} and iid = {};".format(uid,cid))
                                upres = db.commit("update t_inspirer set collections={} where id ={};".format(collections,cid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "取消收藏成功！"
                                data["status"] = 200
                            else:
                                data["data"] = None
                                data["msg"] = "你还没有对该文章收藏过！"
                                data["status"] = 401   
                else:
                    data["data"] = None
                    data["msg"] = "不存在该文章"
                    data["status"] = 401    
            elif collectiontype == "questions":
                qres = db.query("select * from t_questions_user_status where uid = {} and qid = {};".format(uid,cid))
                collections = db.query("select collections from t_questions where id = {} and status = 0;".format(cid))
                if len(collections) != 0 :
                    collections = collections[0]["collections"]
                    if len(qres) == 0:  # 从来没有点过赞
                        if status == 0: # 点赞
                            collections = collections + 1
                            dzres = db.commit("insert into t_questions_user_status (qid,uid,cstatus) values ({},{},0);".format(cid,uid))
                            upres = db.commit("update t_questions set collections={} where id ={};".format(collections,cid))
                            data["data"] = (dzres,upres)
                            data["msg"] = "收藏成功！"
                            data["status"] = 200
                        else:  #取消点赞
                            data["data"] = None
                            data["msg"] = "你还没有对该文章收藏过！"
                            data["status"] = 401  
                    else:
                        cstatus = db.query("select cstatus from t_questions_user_status where qid = {} and uid = {}".format(cid,uid))[0]["cstatus"]
                        if status == 0: # 点赞
                            if cstatus == 0:
                                data["data"] = None
                                data["msg"] = "已经收藏过了"
                                data["status"] = 401                         
                            else:
                                collections = collections + 1
                                dzres = db.commit("update t_questions_user_status set cstatus = 0 where  uid = {} and qid = {};".format(uid,cid))
                                upres = db.commit("update t_questions set collections={} where id ={};".format(collections,cid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "收藏成功！"
                                data["status"] = 200   
                        else: # 取消点赞
                            if cstatus == 0:
                                collections = collections - 1
                                dzres = db.commit("update t_questions_user_status set cstatus = 1 where  uid = {} and qid = {};".format(uid,cid))
                                upres = db.commit("update t_questions set collections={} where id ={};".format(collections,cid))
                                data["data"] = (dzres,upres)
                                data["msg"] = "取消收藏成功！"
                                data["status"] = 200
                            else:
                                data["data"] = None
                                data["msg"] = "你还没有对该文章收藏过！"
                                data["status"] = 401   
                else:
                    data["data"] = None
                    data["msg"] = "不存在该文章"
                    data["status"] = 401    
            else:
                data["data"] = None
                data["msg"] = "不存在该文章类型"
                data["status"] = 401
        else:
            data["msg"] = "状态不正确，仅0或者1"
            data["data"] = None
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