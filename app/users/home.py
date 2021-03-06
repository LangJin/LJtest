from flask import render_template,request
from . import userbp
from ..utils.dbtools import Db
from ..utils.othertools import setcors,is_number,checkctype
from config import db_config
db = Db(db_config)


@userbp.route("/get_title_img",methods=["get"])
def get_title_img():
    '''
    获取首页轮播图
    '''
    res = db.query("select id,title,imghost,rurl from t_title_img where status = 0;")
    return setcors(data=res,status=200)


@userbp.route("/getcoures",methods=["get"])
def getcoures():
    '''
    获取推荐教程
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
    counts = db.query("SELECT count(*) counts FROM t_coures c JOIN t_admin a on c.uid = a.id WHERE c.STATUS = 0;")[0].get("counts")
    if pagenum - counts/10 > 1:
        return setcors(msg="页码超出范围")
    res = db.query("SELECT c.id,c.title,c.content,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_coures c JOIN t_admin a \
            on c.uid = a.id WHERE c.STATUS = 0 order by c.updatetime desc limit {},{};".format(startnum,endnum))
    data = {
        "contentlist":res,
        "counts":counts
    }
    return setcors(data=data,status=200)



@userbp.route("/getquestions",methods=["get"])
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
    counts = db.query("SELECT count(*) counts FROM t_questions c JOIN t_user a on c.uid = a.id WHERE c.STATUS = 0;")[0].get("counts")
    if pagenum - counts/10 > 1:
        return setcors(msg="页码超出范围")
    res = db.query("SELECT c.id,c.title,c.content,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_questions c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 order by c.updatetime desc limit {},{};".format(startnum,endnum))
    data = {
        "contentlist":res,
        "counts":counts
    }
    return setcors(data=data,status=200)


@userbp.route("/get/question",methods=["get"])
def getquestionqid():
    '''
    获取具体的问题内容
    '''
    qid = request.args.get("qid")
    nummsg = is_number(qid)
    if nummsg == True:
        res = db.query("SELECT c.id,c.title,c.content,c.tags,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_questions c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 and c.id = {};".format(qid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=nummsg)


@userbp.route("/getarticle",methods=["get"])
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
    counts = db.query("SELECT count(*) counts FROM t_article c JOIN t_user a on c.uid = a.id WHERE c.STATUS = 0;")[0].get("counts")
    if pagenum - counts/10 > 1:
        return setcors(msg="页码超出范围")
    res = db.query("SELECT c.id,c.title,c.content,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_article c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 order by c.updatetime desc limit {},{};".format(startnum,endnum))
    data = {
        "contentlist":res,
        "counts":counts
    }
    return setcors(data=data,status=200)



@userbp.route("/get/article",methods=["get"])
def getarticleaid():
    '''
    获取具体的文章内容文章
    '''
    aid = request.args.get("aid")
    nummsg = is_number(aid)
    if nummsg == True:
        res = db.query("SELECT c.id,c.title,c.content,c.tags,c.ximg,c.brief,\
            c.goods,c.collections,c.follows,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_article c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 and c.id = {};".format(aid))
        return setcors(data=res,status=200)
    else:
        return setcors(msg=nummsg)


@userbp.route("/getinspirer",methods=["get"])
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
    counts = db.query("select  count(*) counts FROM t_inspirer c JOIN t_user a on c.uid = a.id WHERE c.STATUS = 0;")[0].get("counts")
    if pagenum - counts/10 > 1:
        return setcors(msg="页码超出范围")
    res = db.query("SELECT c.id,c.content,c.ximg,\
            c.goods,c.collections,c.uid,a.nickname,a.userinfo,a.headpic,\
            DATE_FORMAT(c.updatetime, '%Y.%m.%d') times FROM t_inspirer c JOIN t_user a \
            on c.uid = a.id WHERE c.STATUS = 0 order by c.updatetime desc limit {},{};".format(startnum,endnum))
    data = {
        "contentlist":res,
        "counts":counts
    }
    return setcors(data=data,status=200)


@userbp.route("/get/inspirer",methods=["get"])
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


@userbp.route("/gethighusers",methods=["get"])
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


@userbp.route("/getcomments",methods=["post"])
def getcomments():
    '''
    获取评论列表
    '''
    requestdata = request.get_json()
    ctype = requestdata.get("ctype")
    fid = requestdata.get("fid")
    pagenum = requestdata.get("pagenum")
    ctypemsg = checkctype(ctype)
    if ctypemsg != True:
        return setcors(msg="ctype"+ctypemsg)
    fidmsg = is_number(fid)
    if fidmsg != True:
        return setcors(msg="fid"+fidmsg)
    pagenummsg = is_number(pagenum)
    if pagenummsg != True:
        return setcors(msg="pagenum"+pagenummsg)
    else:
        pagenum = int(pagenum)
    endnum = 10
    if pagenum == 1:
        startnum = 0
    else:
        startnum = (pagenum-1)*10
    nummsg = is_number(fid)
    if nummsg == True:
        counts = db.query("select count(*) counts from t_user_comments c join t_user u on c.uid = u.id where c.`status` = 0 and c.ctype = {} and c.fid = {};".format(ctype,fid))[0].get("counts")
        if pagenum - counts/10 > 1:
            return setcors(msg="页码超出范围")
        res = db.query("select c.id,c.`comment`,c.uid,u.headpic,u.userinfo,\
            u.nickname,DATE_FORMAT(c.updatetime,'%Y-%m-%d %T') times \
            from t_user_comments c join t_user u on u.id = c.uid  \
            where c.`status` = 0 and  c.ctype = {} and c.fid = {} order by times desc limit {},{};".format(ctype,fid,startnum,endnum))
        data = {
            "contentlist":res,
            "counts":counts
        }
        return setcors(data=data,status=200)
    else:
        return setcors(msg=nummsg)



@userbp.route("/getmblist",methods=["get"])
def getmblist():
    '''
    获取密保问题列表
    '''
    res = db.query("select id,question from t_user_mbq where status = 0;")
    return setcors(data=res,status=200)


@userbp.route("/gettaglist",methods=["get"])
def gettaglist():
    '''
    获取标签列表
    '''
    ctype = request.args.get("type")
    res = db.query("select tags from t_content_tags where status = 0 and ctype = {};".format(ctype))
    tagslist = []
    for i in range(len(res)):
        tagslist.append(res[i].get("tags"))
    tagslist = list(set(tagslist))
    res = ""
    for i in tagslist:
        res = res+i+","
    tags = {"tags":res[:-1]}
    return setcors(data=tags,status=200)


@userbp.route("/search",methods=["get"])
def search():
    """
    搜索
    0教程1提问2灵感3心得体会,4用户
    """
    value = request.args.get("value")
    ctype = request.args.get("type")
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
    if ctype == "0":
        counts = db.query("select count(*) counts from t_coures a join t_user b on a.uid = b.id where a.status = 0 and a.tags like '%{}%' or a.title like '%{}%';".format(value,value))[0].get("counts")
        res = db.query("select a.id,a.title,a.content,a.ximg,a.brief,a.goods\
            ,a.collections,a.follows,a.uid,b.nickname,b.userinfo,b.headpic,\
                DATE_FORMAT(a.updatetime, '%Y.%m.%d') times from t_coures a \
                    join t_user b on a.uid = b.id where a.status = 0 and a.tags like '%{}%' or a.title like '%{}%' limit {},{};".format(value,value,startnum,endnum))
    elif ctype == "3":
        counts = db.query("select count(*) counts from t_article a join t_user b on a.uid = b.id where a.status = 0 and a.tags like '%{}%' or a.title like '%{}%';".format(value,value))[0].get("counts")
        res = db.query("select a.id,a.title,a.content,a.ximg,a.brief,a.goods,\
            a.collections,a.follows,a.uid,b.nickname,b.userinfo,b.headpic,\
                DATE_FORMAT(a.updatetime, '%Y.%m.%d') times from t_article a \
                    join t_user b on a.uid = b.id where a.status = 0 and a.tags like '%{}%' or a.title like '%{}%' limit {},{};".format(value,value,startnum,endnum))
    elif ctype == "1":
        counts = db.query("select count(*) counts from t_questions a join t_user b on a.uid = b.id where a.status = 0 and a.tags like '%{}%' or a.title like '%{}%';".format(value,value))[0].get("counts")
        res = db.query("select a.id,a.title,a.content,a.ximg,a.brief,a.goods,\
            a.collections,a.follows,a.uid,b.nickname,b.userinfo,b.headpic,\
                DATE_FORMAT(a.updatetime, '%Y.%m.%d') times from t_questions a \
                    join t_user b on a.uid = b.id where a.status = 0 and a.tags like '%{}%' or a.title like '%{}%' limit {},{};".format(value,value,startnum,endnum))
    elif ctype == "2":
        counts = db.query("select count(*) counts from t_inspirer a join t_user b on a.uid = b.id where a.status = 0 and a.content like '%{}%';".format(value))[0].get("counts")
        res = db.query("select a.id,a.content,a.ximg,a.goods,\
            a.collections,a.uid,b.nickname,b.userinfo,b.headpic,\
                DATE_FORMAT(a.updatetime, '%Y.%m.%d') times from t_inspirer a \
                    join t_user b on a.uid = b.id where a.status = 0 and a.content like '%{}%' limit {},{};".format(value,startnum,endnum))
    elif ctype == "4":
        counts = db.query("select count(*) counts from t_user where status = 0 and nickname like '%{}%';".format(value))[0].get("counts")
        res = db.query("select id,nickname,headpic,userinfo from t_user where status = 0 and nickname like '%{}%' limit {},{};".format(value,startnum,endnum))
    else:
        return setcors(msg="不存在该type类型！")
    data = {
        "contentlist":res,
        "counts":counts
    }
    return setcors(data=data,status=200)
