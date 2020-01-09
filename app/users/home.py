from flask import render_template,request
from . import userbp
from ..utils.dbtools import Db
from ..utils.othertools import setcors,is_number
from config import db_config
db = Db(db_config)


@userbp.route("/get_title_img")
def get_title_img():
    '''
    获取首页轮播图
    '''
    res = db.query("select id,title,content,imghost,rurl from t_title_img;")
    return setcors(data=res,status=200)


@userbp.route("/getcoures")
def getcoures():
    '''
    教程
    '''
    pagenum = request.args.get("pagenum")
    if pagenum is None or pagenum == '':
        pagenum = '3'
        res = db.query("SELECT c.id,c.title,c.content,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_coures c JOIN t_admin a \
            on c.uid = a.id WHERE c.STATUS = 0 order by c.updatetime desc limit {};".format(pagenum))
        return setcors(data=res,status=200)
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
    counts = db.query("select  count(*) counts  from t_coures where status = 0;")
    res = db.query("SELECT c.id,c.title,c.content,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_coures c JOIN t_admin a \
            on c.uid = a.id WHERE c.STATUS = 0 order by c.updatetime desc limit {},{};".format(startnum,endnum))
    data = {
        "contentlist":res,
        "counts":counts[0].get("counts")
    }
    return setcors(data=data,status=200)


@userbp.route("/get/coure")
def getcourecid():
    '''
    获取具体的教程内容
    '''
    cid = request.args.get("cid")
    nummsg = is_number(cid)
    if nummsg == True:
        res = db.query("SELECT c.id,c.title,c.content,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_coures c JOIN t_admin a \
            on c.uid = a.id WHERE c.STATUS = 0 and c.id = {};".format(cid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=nummsg)


@userbp.route("/getquestions")
def getquestions():
    '''
    讨论
    '''
    pagenum = request.args.get("pagenum")
    if pagenum is None or pagenum == '':
        pagenum = '3'
        res = db.query("SELECT c.id,c.title,c.content,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_questions c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 order by c.updatetime desc limit {};".format(pagenum))
        return setcors(data=res,status=200)
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
    counts = db.query("select  count(*) counts  from t_questions where status = 0;")
    res = db.query("SELECT c.id,c.title,c.content,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_questions c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 order by c.updatetime desc limit {},{};".format(startnum,endnum))
    data = {
        "contentlist":res,
        "counts":counts[0].get("counts")
    }
    return setcors(data=data,status=200)


@userbp.route("/get/question")
def getquestionqid():
    '''
    获取具体的问题内容
    '''
    qid = request.args.get("qid")
    nummsg = is_number(qid)
    if nummsg == True:
        res = db.query("SELECT c.id,c.title,c.content,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_questions c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 and c.id = {};".format(qid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=nummsg)


@userbp.route("/getarticle")
def getarticle():
    '''
    文章
    '''
    pagenum = request.args.get("pagenum")
    if pagenum is None or pagenum == '':
        pagenum = '4'
        res = db.query("SELECT c.id,c.title,c.content,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_article c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 order by c.updatetime desc limit {};".format(pagenum))
        return setcors(data=res,status=200)
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
    counts = db.query("select  count(*) counts  from t_article where status = 0;")
    res = db.query("SELECT c.id,c.title,c.content,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_article c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 order by c.updatetime desc limit {},{};".format(startnum,endnum))
    data = {
        "contentlist":res,
        "counts":counts[0].get("counts")
    }
    return setcors(data=data,status=200)



@userbp.route("/get/article")
def getarticleaid():
    '''
    获取具体的文章内容文章
    '''
    aid = request.args.get("aid")
    nummsg = is_number(aid)
    if nummsg == True:
        res = db.query("SELECT c.id,c.title,c.content,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_article c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 and c.id = {};".format(aid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=nummsg)


@userbp.route("/getinspirer")
def getinspirer():
    '''
    灵感
    '''
    pagenum = request.args.get("pagenum")
    if pagenum is None or pagenum == '':
        pagenum = '4'
        res = db.query("SELECT c.id,c.content,c.ximg,\
            c.goods,c.collections,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_inspirer c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 order by c.updatetime desc limit {};".format(pagenum))
        return setcors(data=res,status=200)
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
    counts = db.query("select  count(*) counts  from t_inspirer where status = 0;")
    res = db.query("SELECT c.id,c.content,c.ximg,\
            c.goods,c.collections,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_inspirer c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 order by c.updatetime desc limit {},{};".format(startnum,endnum))
    data = {
        "contentlist":res,
        "counts":counts[0].get("counts")
    }
    return setcors(data=data,status=200)


@userbp.route("/get/inspirer")
def getinspireriid():
    '''
    灵感具体内容
    '''
    iid = request.args.get("iid")
    nummsg = is_number(iid)
    if nummsg == True:
        res = db.query("SELECT c.id,c.content,c.ximg,\
            c.goods,c.collections,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_inspirer c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 and c.id = {};".format(iid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=nummsg)


@userbp.route("/gethighusers")
def gethighusers():
    '''
    活跃用户
    '''
    num = request.args.get("num")
    if num is None or num == '':
        num = '15'
    nummsg = is_number(num)
    if nummsg == True:
        res = db.query("select id,nickname,headpic from t_user where status = 0 limit {};".format(num))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=nummsg)


@userbp.route("/get/userinfo")
def getuserinfo():
    '''
    用户主页
    '''
    uid = request.args.get("uid")
    nummsg = is_number(uid)
    if nummsg == True:
        res = db.query("select id,nickname,titlepic,headpic,phone,sex,job,email,weixin,QQ,\
            userinfo,address,DATE_FORMAT(updatetime,'%Y-%m-%d %T') times from t_user where status = 0 and id = {};".format(uid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=nummsg)




@userbp.route("/getcomments",methods=["post"])
def getcomments():
    '''
    getcomments
    '''
    requestdata = request.get_json()
    ctype = requestdata["ctype"]
    fid = requestdata["fid"]
    pagenum = requestdata["pagenum"]
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
    nummsg = is_number(fid)
    if nummsg == True:
        counts = db.query("select count(*) counts from t_user_comments where status = 0 and ctype = {} and fid = {};".format(ctype,fid))
        res = db.query("select c.id,c.`comment`,c.uid,u.headpic,u.userinfo,\
            u.nickname,DATE_FORMAT(c.updatetime,'%Y-%m-%d %T') times \
            from t_user_comments c join t_user u on u.id = c.uid  \
            where c.`status` = 0 and  c.ctype = {} and c.fid = {} order by times desc limit {},{};".format(ctype,fid,startnum,endnum))
        data = {
            "contentlist":res,
            "counts":counts[0].get("counts")
        }
        return setcors(data=data,status=200)
    else:
        return setcors(msg=nummsg)



@userbp.route("/userinspirer")
def userinspirer():
    '''
    获取用户的灵感列表
    '''
    pagenum = request.args.get("pagenum")
    uid = request.args.get("uid")
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
    counts = db.query("select  count(*) counts  from t_inspirer where status = 0 and uid = {};".format(uid))
    res = db.query("SELECT c.id,c.content,c.ximg,\
            c.goods,c.collections,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_inspirer c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 and c.uid = {} order by c.updatetime desc limit {},{};".format(uid,startnum,endnum))
    data = {
        "contentlist":res,
        "counts":counts[0].get("counts")
    }
    return setcors(data=data,status=200)



@userbp.route("/userarticle")
def userarticle():
    '''
    获取用户文章列表
    '''
    pagenum = request.args.get("pagenum")
    uid = request.args.get("uid")
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
    counts = db.query("select  count(*) counts  from t_article where status = 0 and uid = {};".format(uid))
    res = db.query("SELECT c.id,c.title,c.content,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_article c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 and c.uid = {} order by c.updatetime desc limit {},{};".format(uid,startnum,endnum))
    data = {
        "contentlist":res,
        "counts":counts[0].get("counts")
    }
    return setcors(data=data,status=200)


@userbp.route("/userquestions")
def userquestions():
    '''
    用户问题列表
    '''
    pagenum = request.args.get("pagenum")
    uid = request.args.get("uid")
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
    counts = db.query("select  count(*) counts  from t_questions where status = 0 and uid = {};".format(uid))
    res = db.query("SELECT c.id,c.title,c.content,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_questions c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0  and c.uid = {} order by c.updatetime desc limit {},{};".format(uid,startnum,endnum))
    data = {
        "contentlist":res,
        "counts":counts[0].get("counts")
    }
    return setcors(data=data,status=200)


@userbp.route("/getuserfollows",methods=["get"])
def getuserfollows():
    '''
    获取关注人列表
    '''
    uid = request.args.get("uid")
    counts = db.query("select count(*) counts from t_user_follows where status = 0 and uid = {};".format(uid))[0]
    res = db.query("select u.id,u.nickname,u.headpic,u.userinfo,DATE_FORMAT(f.updatetime, '%Y.%m.%d') times from t_user u join t_user_follows f on f.fid = u.id where f.status = 0 and f.uid = {};".format(uid))
    data = {
        "userlist":res,
        "counts":counts.get("counts")
    }
    return setcors(data=data,status=200)


@userbp.route("/getuserfens",methods=["get"])
def getuserfens():
    '''
    获取粉丝列表
    '''
    uid = request.args.get("uid")
    counts = db.query("select count(*) counts from t_user_follows where status = 0 and fid = {};".format(uid))[0]
    res = db.query("select u.id,u.nickname,u.headpic,u.userinfo,DATE_FORMAT(f.updatetime, '%Y.%m.%d') times from \
        t_user u join t_user_follows f on f.uid = u.id where f.status = 0 and f.fid = {}".format(uid))
    data = {
        "userlist":res,
        "counts":counts.get("counts")
    }
    return setcors(data=data,status=200)