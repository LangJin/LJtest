# -*- coding:utf-8 -*-
__author__ = 'LangJin'

from flask import request,session,make_response
from . import userbp
from ..utils.dbtools import Db
from config import db_config
import pymysql
from ..utils.othertools import checkuserinfo,create_token,setcors,checkloginstatus,checkContentType,is_number,checkvalueisNone,encryption,checkphonenum,checkemail
from ..utils.othertools import checkvaluelen
# from werkzeug import secure_filename



db = Db(db_config)


@userbp.route("/regist",methods=["post"])
def regist():
    '''
    用户注册接口\n
    获取json格式的数据进行处理
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    else:
        userinfo = request.get_json()
        username = userinfo.get("username")
        password = userinfo.get("password")
        phone = userinfo.get("phone")
        email = userinfo.get("email")
        valuemsg = checkvalueisNone([username,password,phone,email])
        userregmsg = checkuserinfo(username,password)
        phonemsg = checkphonenum(phone)
        emailmsg = checkemail(email)
        if phonemsg != True:
            return setcors(msg=phonemsg)
        if emailmsg != True:
            return setcors(msg=emailmsg)
        if valuemsg != True:
            return setcors(msg=valuemsg)
        if userregmsg is True:
            sql = "select * from t_user where username = '{}'".format(username)
            res = db.query(sql)
            if len(res) != 0:
                msg = "用户名已存在，请重新设置！"
                return setcors(msg=msg)
            else:
                password = encryption(username,password,"user")
                sql = "insert into t_user (username,password,phone,email) values ('{}','{}','{}','{}');".format(username,password,phone,email)
                dbmsg = db.commit(sql)
                return setcors(msg=dbmsg,status=200)
        else:
            return setcors(msg=userregmsg)



@userbp.route("/login",methods=["post"])
def userlogin():
    '''
    用户登录接口\n
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
            sql = "select * from t_user where status = 0 and username = '{}'".format(username)
            res = db.query(sql)
            if len(res) != 1:
                return setcors(msg="账号不存在或者账号异常")
            else:
                password = encryption(username,password,"user")
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


@userbp.route("/logout",methods=["get"])
def loginout():
    '''
    用户退出登录接口
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        session.clear()
        return setcors(msg="退出成功！",status=200)
    else:
        return setcors(msg=loginstatus)


@userbp.route("/question/new",methods=["post"])
def question():
    '''
    提问接口
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    else:
        requestdata = request.get_json()
        token = request.headers.get("token")
        title = requestdata.get("title")
        brief = requestdata.get("brief")
        ximg = requestdata.get("ximg")
        tags = requestdata.get("tags")
        content = requestdata.get("content")
        valuemsg = checkvalueisNone([title,brief,tags,content])
        titlemsg = checkvaluelen(title,50)
        if valuemsg != True:
            return setcors(msg=valuemsg)
        if titlemsg != True:
            return setcors(msg="标题"+titlemsg)
        loginstatus = checkloginstatus(session,token)
        if loginstatus is True:
            uid = session["userinfo"]["uid"]
            author = session["userinfo"]["nickname"]
            dbres = db.commit("insert into t_questions (title,brief,content,tags,uid,ximg,author) values ('{}','{}','{}','{}',{},'{}','{}');".format(title,brief,content,tags,uid,ximg,author))
            dbqres = db.query("select id from t_questions where uid = {} order by updatetime desc limit 1;".format(uid))[0].get("id")
            data = {
                "questionid":dbqres,
                "status":dbres
            }
            return setcors(data=data,status=200)
        else:
            return setcors(msg=loginstatus)


@userbp.route("/question/update",methods=["post"])
def questionupdate():
    '''
    修改提问接口
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    title = requestdata.get("title")
    brief = requestdata.get("brief")
    tags = requestdata.get("tags")
    content = requestdata.get("content")
    ximg = requestdata.get("ximg")
    valuemsg = checkvalueisNone([title,brief,tags,content,ximg])
    titlemsg = checkvaluelen(title,50)
    if valuemsg != True:
        return setcors(msg=valuemsg)
    if titlemsg != True:
        return setcors(msg="标题"+titlemsg)
    qid = requestdata.get("qid")
    idmsg = is_number(qid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        qres = db.query("select * from t_questions where uid ={} and status = 0 and id = {};".format(uid,qid))
        if len(qres) != 0:
            dbres = db.commit("update t_questions set title='{}',brief='{}',tags='{}',content='{}',ximg = '{}' where id = {} and uid = {};".format(title,brief,tags,content,ximg,qid,uid))
            return setcors(msg=dbres,status=200)
        else:
            return setcors(msg="修改的问题不存在")
    else:
        return setcors(msg=loginstatus)


@userbp.route("/question/delete",methods=["post"])
def questiondelete():
    '''
    删除提问接口
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    qid = requestdata.get("qid")
    idmsg = is_number(qid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginstatus =  checkloginstatus(session,token)
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        qres = db.query("select * from t_questions where uid ={} and status = 0 and id = {};".format(uid,qid))
        if len(qres) != 0:
            dbres = db.commit("update t_questions set status = 1 where id = {} and uid = {};".format(qid,uid))
            return setcors(msg=dbres,status=200)
        else:
            return setcors(msg="删除的问题不存在")
    else:
        return setcors(msg=loginstatus)


@userbp.route("/inspirer/new",methods=["post"])
def inspirer():
    '''
    发表灵感
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    content = requestdata.get("content")
    ximg = requestdata.get("ximg")
    valuemsg = checkvalueisNone([content,ximg])
    contentmsg = checkvaluelen(content,200)
    if valuemsg != True:
        return setcors(msg=valuemsg)
    if contentmsg != True:
        return setcors(msg="内容"+contentmsg)
    ximg = ximg[:-1]
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        author = session["userinfo"]["nickname"]
        dbres = db.commit("insert into t_inspirer (content,uid,author,ximg) values ('{}',{},'{}','{}');".format(content,uid,author,ximg))
        dbqres = db.query("select id from t_inspirer where uid = {} order by updatetime desc limit 1;".format(uid))[0].get("id")
        data = {
            "inspirerid":dbqres,
            "status":dbres
        }
        return setcors(data=data,status=200)
    else:
        return setcors(msg=loginstatus)


@userbp.route("/inspirer/update",methods=["post"])
def inspirerupdate():
    '''
    修改灵感
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    ximg = requestdata.get("ximg")
    content = requestdata.get("content")
    valuemsg = checkvalueisNone([content,ximg])
    contentmsg = checkvaluelen(content,200)
    if valuemsg != True:
        return setcors(msg=valuemsg)
    if contentmsg != True:
        return setcors(msg="内容"+contentmsg)
    ximg = ximg[:-1]
    iid = requestdata.get("iid")
    idmsg = is_number(iid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        qres = db.query("select * from t_inspirer where uid ={} and status = 0 and id = {};".format(uid,iid))
        if len(qres) != 0:
            dbres = db.commit("update t_inspirer set content = '{}',ximg = '{}' where id = {} ;".format(content,ximg,iid))
            return setcors(msg=dbres,status=200)
        else:
            return setcors(msg="修改的灵感不存在！")
    else:
        return setcors(msg=loginstatus)


@userbp.route("/inspirer/delete",methods=["post"])
def inspirerdelete():
    '''
    删除灵感
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    questiondata = request.get_json()
    iid = questiondata.get("iid")
    idmsg = is_number(iid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        ires = db.query("select * from t_inspirer where uid = {} and status = 0 and id = {};".format(uid,iid))
        if len(ires) != 0:
            dbres = db.commit("update t_inspirer set status = 1 where id = {};".format(iid))
            return setcors(msg=dbres,status=200)
        else:
            return setcors(msg="删除的灵感不存在！")   
    else:
        return setcors(msg=loginstatus)


@userbp.route("/article/new",methods=["post"])
def article():
    '''
    写文章接口
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    title = requestdata.get("title")
    tags = requestdata.get("tags")
    content = requestdata.get("content")
    brief = requestdata.get("brief")
    ximg = requestdata.get("ximg")
    valuemsg = checkvalueisNone([title,brief,tags,content])
    titlemsg = checkvaluelen(title,50)
    if valuemsg != True:
        return setcors(msg=valuemsg)
    if titlemsg != True:
        return setcors(msg="标题"+titlemsg)
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        author = session["userinfo"]["nickname"]
        dbres = db.commit("insert into t_article (title,brief,content,tags,uid,author,ximg) values ('{}','{}','{}','{}',{},'{}','{}');".format(title,brief,content,tags,uid,author,ximg))
        dbqres = db.query("select id from t_article where uid = {} order by updatetime desc limit 1".format(uid))[0].get("id")
        data = {
            "articleid":dbqres,
            "status":dbres
        }
        return setcors(data=data,status=200)
    else:
        return setcors(msg=loginstatus)


@userbp.route("/article/update",methods=["post"])
def articleupdate():
    '''
    修改文章接口
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    title = requestdata.get("title")
    tags = requestdata.get("tags")
    content = requestdata.get("content")
    brief = requestdata.get("brief")
    ximg = requestdata.get("ximg")
    valuemsg = checkvalueisNone([title,brief,tags,content,ximg])
    titlemsg = checkvaluelen(title,50)
    if valuemsg != True:
        return setcors(msg=valuemsg)
    if titlemsg != True:
        return setcors(msg="标题"+titlemsg)
    aid = requestdata.get("aid")
    idmsg = is_number(aid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if checkloginstatus(session,token) is True:
        uid = session["userinfo"]["uid"]
        ares = db.query("select * from t_article where status =0 and uid ={} and id = {};".format(uid,aid))
        if len(ares) != 0: 
            dbres = db.commit("update t_article set title='{}',tags='{}',content='{}',brief = '{}',ximg = '{}' where id ={};".format(title,tags,content,brief,ximg,aid))
            return setcors(msg=dbres,status=200)
        else:
            return setcors(msg="修改的文章不存在！")
    else:
        return setcors(msg=loginstatus)


@userbp.route("/article/delete",methods=["post"])
def articledelete():
    '''
    删除文章接口
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    aid = requestdata.get("aid")
    idmsg = is_number(aid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        ares = db.query("select * from t_article where status =0 and uid ={} and id = {};".format(uid,aid))
        if len(ares) != 0: 
            dbres = db.commit("update t_article set status=1 where id ={} and uid = {};".format(aid,uid))
            return setcors(msg=dbres,status=200)
        else:
            return setcors(msg="删除的文章不存在")
    else:
        return setcors(msg=loginstatus)


@userbp.route("/updateuserinfo",methods=["post"])
def updateuserinfo():
    '''
    修改个人资料接口
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    nickname = requestdata.get("nickname")
    phone = requestdata.get("phone")
    sex = requestdata.get("sex")
    job = requestdata.get("job")
    email = requestdata.get("email")
    weixin = requestdata.get("weixin")
    qq = requestdata.get("qq")
    qianming = requestdata.get("userinfo")
    address = requestdata.get("address")
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        dbres = db.commit("update t_user set nickname='{}', phone='{}', sex='{}', job='{}', email='{}',\
        weixin ='{}', QQ='{}', userinfo='{}', address='{}' where id={};".format(nickname,phone,sex,job,email,weixin,qq,qianming,address,uid))
        return setcors(msg=dbres,status=200)
    else:
        return setcors(msg=loginstatus)


@userbp.route("/updateuserheadpic",methods=["post"])
def updateuserheadpic():
    '''
    修改个人头像接口
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    headpic = requestdata.get("ximg")
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        dbres = db.commit("update t_user set headpic='{}' where id={};".format(headpic,uid))
        return setcors(msg=dbres,status=200)
    else:
        return setcors(msg=loginstatus)

@userbp.route("/updateusertitlepic",methods=["post"])
def updateusertitlepic():
    '''
    修改个人title图接口
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    titlepic = requestdata.get("ximg")
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        dbres = db.commit("update t_user set titlepic='{}' where id={};".format(titlepic,uid))
        return setcors(msg=dbres,status=200)
    else:
        return setcors(msg=loginstatus)


@userbp.route("/userfellgoods",methods=["post"])
def userfellgoods():
    '''
    点赞 # {"ctype":"0","status":0,"gid":1}
    0教程1提问2灵感3心得体会
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    ctype = str(requestdata.get("ctype"))
    status = requestdata.get("status")
    gid = requestdata.get("gid")
    idmsg = is_number(gid)
    if idmsg != True:
        return setcors(msg=idmsg)
    if status not in [0,1,"0","1"]:
        return setcors(msg="status仅为0或者1")
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        if ctype == "3":
            qres = db.query("select * from t_article_user_status where uid = {} and aid = {};".format(uid,gid))
            goods = db.query("select goods from t_article where id = {} and status = 0;".format(gid))
            if len(goods) != 0 :
                goods = goods[0]["goods"]
                if len(qres) == 0:  # 从来没有点过赞
                    if status == 0: # 点赞
                        goods = goods + 1
                        dzres = db.commit("insert into t_article_user_status (aid,uid,gstatus) values ({},{},0);".format(gid,uid))
                        upres = db.commit("update t_article set goods={} where id ={};".format(goods,gid))
                        return setcors(msg=(dzres,upres),status=200)
                    else:  #取消点赞
                        return setcors(msg="你还没有对该文章点赞过！")
                else:
                    gstatus = db.query("select gstatus from t_article_user_status where aid = {} and uid = {};".format(gid,uid))[0]["gstatus"]
                    if status == 0: # 点赞
                        if gstatus == 0:  
                            return setcors(msg="已经点过赞了")                    
                        else:
                            goods = goods + 1
                            dzres = db.commit("update t_article_user_status set gstatus = 0 where  uid = {} and aid = {};".format(uid,gid))
                            upres = db.commit("update t_article set goods={} where id ={};".format(goods,gid))
                            return setcors(msg=(dzres,upres),status=200) 
                    else: # 取消点赞
                        if gstatus == 0:
                            goods = goods - 1
                            dzres = db.commit("update t_article_user_status set gstatus = 1 where  uid = {} and aid = {};".format(uid,gid))
                            upres = db.commit("update t_article set goods={} where id ={};".format(goods,gid))
                            return setcors(msg=(dzres,upres),status=200) 
                        else:
                            return setcors(msg="你还没有对该文章点赞过！") 
            else:        
                return setcors(msg="不存在该文章")     
        elif ctype == "0":
            qres = db.query("select * from t_coures_user_status where uid = {} and cid = {};".format(uid,gid))
            goods = db.query("select goods from t_coures where id = {} and status = 0;".format(gid))
            if len(goods) != 0 :
                goods = goods[0]["goods"]
                if len(qres) == 0:  # 从来没有点过赞
                    if status == 0: # 点赞
                        goods = goods + 1
                        dzres = db.commit("insert into t_coures_user_status (cid,uid,gstatus) values ({},{},0);".format(gid,uid))
                        upres = db.commit("update t_coures set goods={} where id ={};".format(goods,gid))
                        return setcors(msg=(dzres,upres),status=200) 
                    else:  #取消点赞
                        return setcors(msg="你还没有对该教程点赞过！")  
                else:
                    gstatus = db.query("select gstatus from t_coures_user_status where cid = {} and uid = {};".format(gid,uid))[0]["gstatus"]
                    if status == 0: # 点赞
                        if gstatus == 0:   
                            return setcors(msg="已经点过赞了")                      
                        else:
                            goods = goods + 1
                            dzres = db.commit("update t_coures_user_status set gstatus = 0 where  uid = {} and cid = {};".format(uid,gid))
                            upres = db.commit("update t_coures set goods={} where id ={};".format(goods,gid))
                            return setcors(msg=(dzres,upres),status=200)  
                    else: # 取消点赞
                        if gstatus == 0:
                            goods = goods - 1
                            dzres = db.commit("update t_coures_user_status set gstatus = 1 where  uid = {} and cid = {};".format(uid,gid))
                            upres = db.commit("update t_coures set goods={} where id ={};".format(goods,gid))
                            return setcors(msg=(dzres,upres),status=200) 
                        else:
                            return setcors(msg="你还没有对该教程点赞过！")     
            else:
                return setcors(msg="不存在该教程")   
        elif ctype == "2":
            qres = db.query("select * from t_inspirer_user_status where uid = {} and iid = {};".format(uid,gid))
            goods = db.query("select goods from t_inspirer where id = {} and status = 0;".format(gid))
            if len(goods) != 0 :
                goods = goods[0]["goods"]
                if len(qres) == 0:  # 从来没有点过赞
                    if status == 0: # 点赞
                        goods = goods + 1
                        dzres = db.commit("insert into t_inspirer_user_status (iid,uid,gstatus) values ({},{},0);".format(gid,uid))
                        upres = db.commit("update t_inspirer set goods={} where id ={};".format(goods,gid))
                        return setcors(msg=(dzres,upres),status=200) 
                    else:  #取消点赞
                        return setcors(msg="你还没有对该灵感点赞过！") 
                else:
                    gstatus = db.query("select gstatus from t_inspirer_user_status where iid = {} and uid = {}".format(gid,uid))[0]["gstatus"]
                    if status == 0: # 点赞
                        if gstatus == 0:
                            return setcors(msg="已经点过赞了")                       
                        else:
                            goods = goods + 1
                            dzres = db.commit("update t_inspirer_user_status set gstatus = 0 where  uid = {} and iid = {};".format(uid,gid))
                            upres = db.commit("update t_inspirer set goods={} where id ={};".format(goods,gid))
                            return setcors(msg=(dzres,upres),status=200)   
                    else: # 取消点赞
                        if gstatus == 0:
                            goods = goods - 1
                            dzres = db.commit("update t_inspirer_user_status set gstatus = 1 where  uid = {} and iid = {};".format(uid,gid))
                            upres = db.commit("update t_inspirer set goods={} where id ={};".format(goods,gid))
                            return setcors(msg=(dzres,upres),status=200) 
                        else:  
                            return setcors(msg="你还没有对该灵感点赞过！") 
            else: 
                return setcors(msg="不存在该灵感") 
        elif ctype == "1":
            qres = db.query("select * from t_questions_user_status where uid = {} and qid = {};".format(uid,gid))
            goods = db.query("select goods from t_questions where id = {} and status = 0;".format(gid))
            if len(goods) != 0 :
                goods = goods[0]["goods"]
                if len(qres) == 0:  # 从来没有点过赞
                    if status == 0: # 点赞
                        goods = goods + 1
                        dzres = db.commit("insert into t_questions_user_status (qid,uid,gstatus) values ({},{},0);".format(gid,uid))
                        upres = db.commit("update t_questions set goods={} where id ={};".format(goods,gid))
                        return setcors(msg=(dzres,upres),status=200) 
                    else:  #取消点赞
                        return setcors(msg="你还没有对该问题点赞过！")
                else:
                    gstatus = db.query("select gstatus from t_questions_user_status where qid = {} and uid = {};".format(gid,uid))[0]["gstatus"]
                    if status == 0: # 点赞
                        if gstatus == 0:
                            return setcors(msg="已经点过赞了")                       
                        else:
                            goods = goods + 1
                            dzres = db.commit("update t_questions_user_status set gstatus = 0 where  uid = {} and qid = {};".format(uid,gid))
                            upres = db.commit("update t_questions set goods={} where id ={};".format(goods,gid))
                            return setcors(msg=(dzres,upres),status=200)    
                    else: # 取消点赞
                        if gstatus == 0:
                            goods = goods - 1
                            dzres = db.commit("update t_questions_user_status set gstatus = 1 where  uid = {} and qid = {};".format(uid,gid))
                            upres = db.commit("update t_questions set goods={} where id ={};".format(goods,gid))
                            return setcors(msg=(dzres,upres),status=200) 
                        else: 
                            return setcors(msg="你还没有对该问题点赞过！") 
            else:
                return setcors(msg="不存在该问题")    
        else:
            return setcors(msg="ctype类型不正确！")
    else:
        return setcors(msg=loginstatus)



@userbp.route("/usercollections",methods=["post"])
def usercollections():
    '''
    收藏  # {"ctype":"0","status":0,"cid":1}
    0教程1提问2灵感3心得体会
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    ctype = str(requestdata.get("ctype"))
    status = requestdata.get("status")
    if status not in [0,1,"0","1"]:
        return setcors(msg="status仅能为0或1")
    cid = requestdata.get("cid")
    idmsg = is_number(cid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token) 
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        if ctype == "3":
            qres = db.query("select * from t_article_user_status where uid = {} and aid = {};".format(uid,cid))
            collections = db.query("select collections from t_article where id = {}  and status = 0;".format(cid))
            if len(collections) != 0 :
                collections = collections[0]["collections"]
                if len(qres) == 0:  # 从来没有点过赞
                    if status == 0: # 点赞
                        collections = collections + 1
                        dzres = db.commit("insert into t_article_user_status (aid,uid,cstatus) values ({},{},0);".format(cid,uid))
                        upres = db.commit("update t_article set collections={} where id ={};".format(collections,cid))
                        return setcors(msg=(dzres,upres),status=200)
                    else:  #取消点赞
                        return setcors(msg="你还没有对该文章收藏过！")
                else:
                    cstatus = db.query("select cstatus from t_article_user_status where aid = {} and uid = {};".format(cid,uid))[0]["cstatus"]
                    if status == 0: # 点赞
                        if cstatus == 0:     
                            return setcors(msg="已经收藏过了")                 
                        else:
                            collections = collections + 1
                            dzres = db.commit("update t_article_user_status set cstatus = 0 where  uid = {} and aid = {};".format(uid,cid))
                            upres = db.commit("update t_article set collections={} where id ={};".format(collections,cid))
                            return setcors(msg=(dzres,upres),status=200) 
                    else: # 取消点赞
                        if cstatus == 0:
                            collections = collections - 1
                            dzres = db.commit("update t_article_user_status set cstatus = 1 where  uid = {} and aid = {};".format(uid,cid))
                            upres = db.commit("update t_article set collections={} where id ={};".format(collections,cid))
                            return setcors(msg=(dzres,upres),status=200)
                        else:
                            return setcors(msg="你还没有对该文章收藏过！")
            else:
                return setcors(msg="不存在该文章")          
        elif ctype == "0":
            qres = db.query("select * from t_coures_user_status where uid = {} and cid = {};".format(uid,cid))
            collections = db.query("select collections from t_coures where id = {} and status = 0;".format(cid))
            if len(collections) != 0 :
                collections = collections[0]["collections"]
                if len(qres) == 0:  # 从来没有点过赞
                    if status == 0: # 点赞
                        collections = collections + 1
                        dzres = db.commit("insert into t_coures_user_status (cid,uid,cstatus) values ({},{},0);".format(cid,uid))
                        upres = db.commit("update t_coures set collections={} where id ={};".format(collections,cid))
                        return setcors(msg=(dzres,upres),status=200)
                    else:  #取消点赞
                        return setcors(msg="你还没有对该文章收藏过！")
                else:
                    cstatus = db.query("select cstatus from t_coures_user_status where cid = {} and uid = {};".format(cid,uid))[0]["cstatus"]
                    if status == 0: # 点赞
                        if cstatus == 0:  
                            return setcors(msg="已经收藏过了")                    
                        else:
                            collections = collections + 1
                            dzres = db.commit("update t_coures_user_status set cstatus = 0 where  uid = {} and cid = {};".format(uid,cid))
                            upres = db.commit("update t_coures set collections={} where id ={};".format(collections,cid))
                            return setcors(msg=(dzres,upres),status=200)   
                    else: # 取消点赞
                        if cstatus == 0:
                            collections = collections - 1
                            dzres = db.commit("update t_coures_user_status set cstatus = 1 where  uid = {} and cid = {};".format(uid,cid))
                            upres = db.commit("update t_coures set collections={} where id ={};".format(collections,cid))
                            return setcors(msg=(dzres,upres),status=200)
                        else:
                            return setcors(msg="你还没有对该文章收藏过！")   
            else: 
                return setcors(msg="不存在该教程")
        elif ctype == "2":
            qres = db.query("select * from t_inspirer_user_status where uid = {} and iid = {};".format(uid,cid))
            collections = db.query("select collections from t_inspirer where id = {} and status = 0;".format(cid))
            if len(collections) != 0 :
                collections = collections[0]["collections"]
                if len(qres) == 0:  # 从来没有点过赞
                    if status == 0: # 点赞
                        collections = collections + 1
                        dzres = db.commit("insert into t_inspirer_user_status (iid,uid,cstatus) values ({},{},0);".format(cid,uid))
                        upres = db.commit("update t_inspirer set collections={} where id ={};".format(collections,cid))
                        return setcors(msg=(dzres,upres),status=200) 
                    else:  #取消点赞
                        return setcors(msg="你还没有对该文章收藏过！")
                else:
                    cstatus = db.query("select cstatus from t_inspirer_user_status where iid = {} and uid = {};".format(cid,uid))[0]["cstatus"]
                    if status == 0: # 点赞
                        if cstatus == 0:   
                            return setcors(msg="已经收藏过了")                  
                        else:
                            collections = collections + 1
                            dzres = db.commit("update t_inspirer_user_status set cstatus = 0 where  uid = {} and iid = {};".format(uid,cid))
                            upres = db.commit("update t_inspirer set collections={} where id ={};".format(collections,cid))
                            return setcors(msg=(dzres,upres),status=200)  
                    else: # 取消点赞
                        if cstatus == 0:
                            collections = collections - 1
                            dzres = db.commit("update t_inspirer_user_status set cstatus = 1 where  uid = {} and iid = {};".format(uid,cid))
                            upres = db.commit("update t_inspirer set collections={} where id ={};".format(collections,cid))
                            return setcors(msg=(dzres,upres),status=200)
                        else:
                            return setcors(msg="你还没有对该文章收藏过！")
            else:
                return setcors(msg="不存在该文章")
        elif ctype == "1":
            qres = db.query("select * from t_questions_user_status where uid = {} and qid = {};".format(uid,cid))
            collections = db.query("select collections from t_questions where id = {} and status = 0;".format(cid))
            if len(collections) != 0 :
                collections = collections[0]["collections"]
                if len(qres) == 0:  # 从来没有点过赞
                    if status == 0: # 点赞
                        collections = collections + 1
                        dzres = db.commit("insert into t_questions_user_status (qid,uid,cstatus) values ({},{},0);".format(cid,uid))
                        upres = db.commit("update t_questions set collections={} where id ={};".format(collections,cid))
                        return setcors(msg=(dzres,upres),status=200)
                    else:  #取消点赞
                        return setcors(msg="你还没有对该文章收藏过！")
                else:
                    cstatus = db.query("select cstatus from t_questions_user_status where qid = {} and uid = {}".format(cid,uid))[0]["cstatus"]
                    if status == 0: # 点赞
                        if cstatus == 0:    
                            return setcors(msg="已经收藏过了")               
                        else:
                            collections = collections + 1
                            dzres = db.commit("update t_questions_user_status set cstatus = 0 where  uid = {} and qid = {};".format(uid,cid))
                            upres = db.commit("update t_questions set collections={} where id ={};".format(collections,cid))
                            return setcors(msg=(dzres,upres),status=200)
                    else: # 取消点赞
                        if cstatus == 0:
                            collections = collections - 1
                            dzres = db.commit("update t_questions_user_status set cstatus = 1 where  uid = {} and qid = {};".format(uid,cid))
                            upres = db.commit("update t_questions set collections={} where id ={};".format(collections,cid))
                            return setcors(msg=(dzres,upres),status=200)
                        else:
                            return setcors(msg="你还没有对该文章收藏过！")
            else:
                return setcors(msg="不存在该文章")
        else:
            return setcors(msg="不存在该文章类型")
    else:
        return setcors(msg=loginstatus)



@userbp.route("/userfollows",methods=["post"])
def userfollows():
    '''
    关注  # {"ctype":"0","status":0,"fid":1}
    0教程1提问2灵感3心得体会
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    ctype = requestdata.get("ctype")
    status = requestdata.get("status")
    if status not in [0,1,"0","1"]:
        return setcors(msg="status仅能为0或1")
    fid = requestdata.get("fid")
    idmsg = is_number(fid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token) 
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        if ctype == "3":
            qres = db.query("select * from t_article_user_status where uid = {} and aid = {};".format(uid,fid))
            follows = db.query("select follows from t_article where id = {}  and status = 0;".format(fid))
            if len(follows) != 0 :
                follows = follows[0]["follows"]
                if len(qres) == 0:  # 从来没有点过赞
                    if status == 0: # 点赞
                        follows = follows + 1
                        dzres = db.commit("insert into t_article_user_status (aid,uid,fstatus) values ({},{},0);".format(fid,uid))
                        upres = db.commit("update t_article set follows={} where id ={};".format(follows,fid))
                        return setcors(msg=(dzres,upres),status=200)
                    else:  #取消点赞
                        return setcors(msg="你还没有对该文章关注过！")
                else:
                    fstatus = db.query("select fstatus from t_article_user_status where aid = {} and uid = {};".format(fid,uid))[0]["fstatus"]
                    if status == 0: # 点赞
                        if fstatus == 0:     
                            return setcors(msg="已经关注过了")                 
                        else:
                            follows = follows + 1
                            dzres = db.commit("update t_article_user_status set fstatus = 0 where  uid = {} and aid = {};".format(uid,fid))
                            upres = db.commit("update t_article set follows={} where id ={};".format(follows,fid))
                            return setcors(msg=(dzres,upres),status=200) 
                    else: # 取消点赞
                        if fstatus == 0:
                            follows = follows - 1
                            dzres = db.commit("update t_article_user_status set fstatus = 1 where  uid = {} and aid = {};".format(uid,fid))
                            upres = db.commit("update t_article set follows={} where id ={};".format(follows,fid))
                            return setcors(msg=(dzres,upres),status=200)
                        else:
                            return setcors(msg="你还没有对该文章关注过！")
            else:
                return setcors(msg="不存在该文章")          
        elif ctype == "0":
            qres = db.query("select * from t_coures_user_status where uid = {} and cid = {};".format(uid,fid))
            follows = db.query("select follows from t_coures where id = {} and status = 0;".format(fid))
            if len(follows) != 0 :
                follows = follows[0]["follows"]
                if len(qres) == 0:  # 从来没有点过赞
                    if status == 0: # 点赞
                        follows = follows + 1
                        dzres = db.commit("insert into t_coures_user_status (cid,uid,fstatus) values ({},{},0);".format(fid,uid))
                        upres = db.commit("update t_coures set follows={} where id ={};".format(follows,fid))
                        return setcors(msg=(dzres,upres),status=200)
                    else:  #取消点赞
                        return setcors(msg="你还没有对该文章关注过！")
                else:
                    fstatus = db.query("select fstatus from t_coures_user_status where cid = {} and uid = {};".format(fid,uid))[0]["fstatus"]
                    if status == 0: # 点赞
                        if fstatus == 0:  
                            return setcors(msg="已经关注过了")                    
                        else:
                            follows = follows + 1
                            dzres = db.commit("update t_coures_user_status set fstatus = 0 where  uid = {} and cid = {};".format(uid,fid))
                            upres = db.commit("update t_coures set follows={} where id ={};".format(follows,fid))
                            return setcors(msg=(dzres,upres),status=200)   
                    else: # 取消点赞
                        if fstatus == 0:
                            follows = follows - 1
                            dzres = db.commit("update t_coures_user_status set fstatus = 1 where  uid = {} and cid = {};".format(uid,fid))
                            upres = db.commit("update t_coures set follows={} where id ={};".format(follows,fid))
                            return setcors(msg=(dzres,upres),status=200)
                        else:
                            return setcors(msg="你还没有对该文章关注过！")   
            else: 
                return setcors(msg="不存在该教程")
        elif ctype == "1":
            qres = db.query("select * from t_questions_user_status where uid = {} and qid = {};".format(uid,fid))
            follows = db.query("select follows from t_questions where id = {} and status = 0;".format(fid))
            if len(follows) != 0 :
                follows = follows[0]["follows"]
                if len(qres) == 0:  # 从来没有点过赞
                    if status == 0: # 点赞
                        follows = follows + 1
                        dzres = db.commit("insert into t_questions_user_status (qid,uid,fstatus) values ({},{},0);".format(fid,uid))
                        upres = db.commit("update t_questions set follows={} where id ={};".format(follows,fid))
                        return setcors(msg=(dzres,upres),status=200)
                    else:  #取消点赞
                        return setcors(msg="你还没有对该文章关注过！")
                else:
                    fstatus = db.query("select fstatus from t_questions_user_status where qid = {} and uid = {}".format(fid,uid))[0]["fstatus"]
                    if status == 0: # 点赞
                        if fstatus == 0:    
                            return setcors(msg="已经关注过了")               
                        else:
                            follows = follows + 1
                            dzres = db.commit("update t_questions_user_status set fstatus = 0 where  uid = {} and qid = {};".format(uid,fid))
                            upres = db.commit("update t_questions set follows={} where id ={};".format(follows,fid))
                            return setcors(msg=(dzres,upres),status=200)
                    else: # 取消点赞
                        if fstatus == 0:
                            follows = follows - 1
                            dzres = db.commit("update t_questions_user_status set fstatus = 1 where  uid = {} and qid = {};".format(uid,fid))
                            upres = db.commit("update t_questions set follows={} where id ={};".format(follows,fid))
                            return setcors(msg=(dzres,upres),status=200)
                        else:
                            return setcors(msg="你还没有对该文章关注过！")
            else:
                return setcors(msg="不存在该文章")
        else:
            return setcors(msg="不存在该文章类型")
    else:
        return setcors(msg=loginstatus)


@userbp.route("/comment/new",methods=["post"])
def usercomment():
    '''
    文章类型，0教程1提问2灵感3心得体会4评论
    评论  # {"ctype":"0","comment":0,"fid":1}
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    ctype = requestdata.get("ctype")
    if ctype not in ["0","1","2","3","4",0,1,2,3,4]:
        return setcors(msg="ctype类型不正确！")
    comment = requestdata.get("comment")
    fid = requestdata.get("fid")
    valuemsg = checkvalueisNone([ctype,comment,fid])
    commentmsg = checkvaluelen(comment,500)
    if valuemsg != True:
        return setcors(msg=valuemsg)
    if commentmsg != True:
        return setcors(msg="评论"+commentmsg)
    idmsg = is_number(fid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token) 
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        author = session["userinfo"]["nickname"]
        dbres = db.commit("insert into t_user_comments (ctype,fid,uid,comment,author) values ('{}',{},{},'{}','{}');".format(ctype,fid,uid,comment,author))
        return setcors(msg=dbres,status=200)
    else:
        return setcors(msg=loginstatus)


@userbp.route("/comment/update",methods=["post"])
def usercommentupdate():
    '''
    修改评论  # {"comment":0,"cid":1}
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    comment = requestdata.get("comment")
    cid = requestdata.get("cid")
    valuemsg = checkvalueisNone([comment,cid])
    if valuemsg != True:
        return setcors(msg=valuemsg)
    idmsg = is_number(cid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token) 
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        comments = db.query("select comment from t_user_comments where id = {} and uid ={} and status = 0;".format(cid,uid))
        if len(comments) != 0:
            dbres = db.commit("update t_user_comments set comment = '{}' where id = {};".format(comment,cid))
            return setcors(msg=dbres,status=200)
        else:
            return setcors(msg="修改的评论不存在")
    else:
        return setcors(msg=loginstatus)


@userbp.route("/comment/delete",methods=["post"])
def usercommentdelete():
    '''
    删除评论  # {"cid":1}
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    cid = requestdata.get("cid")
    idmsg = is_number(cid)
    if idmsg != True:
        return setcors(msg=idmsg)
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token) 
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        comments = db.query("select comment from t_user_comments where id = {} and uid ={} and status = 0;".format(cid,uid))
        if len(comments) != 0:
            dbres = db.commit("update t_user_comments set status = 1 where id = {};".format(cid))
            return setcors(msg=dbres,status=200)
        else:
            return setcors(msg="删除的评论不存在")
    else:
        return setcors(msg=loginstatus)


@userbp.route("/getuser4status",methods=["post"])
def getuser4status():
    '''
    状态{"ctype":"","fid":""}
    0教程1提问2灵感3心得体会
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    requestdata = request.get_json()
    ctype = str(requestdata.get("ctype"))
    fid = requestdata.get("fid")
    valuemsg = checkvalueisNone([ctype,fid])
    if valuemsg != True:
        return setcors(msg=valuemsg)
    token = request.headers.get("token")
    loginstatus = checkloginstatus(session,token) 
    if loginstatus is True:
        uid = session["userinfo"]["uid"]
        if ctype == "0":
            dbres = db.query("select gstatus,fstatus,cstatus from t_coures_user_status where cid = {} and uid = {};".format(fid,uid))
        elif ctype == "3":
            dbres = db.query("select gstatus,fstatus,cstatus from t_article_user_status where aid = {} and uid = {};".format(fid,uid))
        elif ctype == "2":
            dbres = db.query("select gstatus,fstatus,cstatus from t_inspirer_user_status where iid = {} and uid = {};".format(fid,uid))
        elif ctype == "1":
            dbres = db.query("select gstatus,fstatus,cstatus from t_questions_user_status where qid = {} and uid = {};".format(fid,uid))
        else:
            return setcors(msg="不存在该类型！")
        return setcors(data=dbres,status=200)
    else:
        return setcors(msg=loginstatus)




@userbp.route("/test")
def test():
    headers  = request.args.get("token")
    return setcors(data=headers,status=200)