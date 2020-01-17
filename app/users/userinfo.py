
from flask import request
from . import userbp
from ..utils.dbtools import Db
from ..utils.othertools import setcors,is_number
from config import db_config
db = Db(db_config)



@userbp.route("/get/userinfo")
def getuserinfo():
    '''
    用户主页
    '''
    uid = request.args.get("uid")
    nummsg = is_number(uid)
    if nummsg == True:
        res = db.query("select id,nickname,titlepic,headpic,userinfo,email,job from t_user where status = 0 and id = {};".format(uid))
        follows = db.query("select count(*) counts from t_user_follows where status = 0 and uid = {};".format(uid))[0].get("counts")
        fens = db.query("select count(*) counts from t_user_follows where status = 0 and fid = {};".format(uid))[0].get("counts")
        data = {
            "userinfo":res,
            "follows":follows,
            "fens":fens
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


@userbp.route("/userquestions",methods=["get"])
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



@userbp.route("/getuserdt",methods=["get"])
def getuserdt():
    '''
    获取用户动态列表
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
    sql = "select * from (\
        select '发表了问题'  as dt,id,title,1 as ctype,uid,ximg,DATE_FORMAT(updatetime, '%Y.%m.%d %T') times from t_article UNION \
        select '发表了文章',id,title,3,uid,ximg,DATE_FORMAT(updatetime, '%Y.%m.%d %T') times from t_questions UNION \
        select '发表了灵感',id,content,2,uid,ximg,DATE_FORMAT(updatetime, '%Y.%m.%d %T') times from t_inspirer UNION \
        select '点赞了',b.id,b.title,0,a.uid,b.ximg,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_coures_user_status a join t_coures b on a.cid = b.id where gstatus = 0 UNION \
        select '收藏了',b.id,b.title,0,a.uid,b.ximg,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_coures_user_status a join t_coures b on a.cid = b.id  where cstatus = 0 UNION \
        select '关注了',b.id,b.title,0,a.uid,b.ximg,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_coures_user_status  a join t_coures b on a.cid = b.id where fstatus = 0 UNION \
        select '点赞了',b.id,b.title,3,a.uid,b.ximg,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_article_user_status a join t_article b on a.aid = b.id where gstatus = 0 UNION \
        select '收藏了',b.id,b.title,3,a.uid,b.ximg,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_article_user_status a join t_article b on a.aid = b.id  where cstatus = 0 UNION \
        select '关注了',b.id,b.title,3,a.uid,b.ximg,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_article_user_status  a join t_article b on a.aid = b.id where fstatus = 0 UNION \
        select '点赞了',b.id,b.content,2,a.uid,b.ximg,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_inspirer_user_status a join t_inspirer b on a.iid = b.id where gstatus = 0 UNION \
        select '收藏了',b.id,b.content,2,a.uid,b.ximg,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_inspirer_user_status a join t_inspirer b on a.iid = b.id  where cstatus = 0 UNION \
        select '点赞了',b.id,b.title,1,a.uid,b.ximg,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_questions_user_status a join t_questions b on a.qid = b.id where gstatus = 0 UNION \
        select '收藏了',b.id,b.title,1,a.uid,b.ximg,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_questions_user_status a join t_questions b on a.qid = b.id  where cstatus = 0 UNION \
        select '关注了',b.id,b.title,1,a.uid,b.ximg,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_questions_user_status  a join t_questions b on a.qid = b.id where fstatus = 0 \
        ) as a where uid = {} order by times desc limit {},{}; ".format(uid,startnum,endnum)
    res = db.query(sql=sql)
    data = {
        "userlist":res,
        "counts":88
    }
    return setcors(data=data,status=200)

'''
select * from (
    select '发表了问题'  as dt,id,title,1 as ctype,uid,DATE_FORMAT(updatetime, '%Y.%m.%d %T') times from t_article UNION 
    select '发表了文章',id,title,3,uid,DATE_FORMAT(updatetime, '%Y.%m.%d %T') times from t_questions UNION
    select '发表了灵感',id,content,2,uid,DATE_FORMAT(updatetime, '%Y.%m.%d %T') times from t_inspirer UNION
    -- select '评论',id,comment,4,uid,DATE_FORMAT(updatetime, '%Y.%m.%d %T') times from t_user_comments UNION 
    select '点赞了',b.id,b.title,0,a.uid,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_coures_user_status a join t_coures b on a.cid = b.id where gstatus = 0 UNION
    select '收藏了',b.id,b.title,0,a.uid,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_coures_user_status a join t_coures b on a.cid = b.id  where cstatus = 0 UNION
    select '关注了',b.id,b.title,0,a.uid,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_coures_user_status  a join t_coures b on a.cid = b.id where fstatus = 0 UNION
    select '点赞了',b.id,b.title,3,a.uid,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_article_user_status a join t_article b on a.aid = b.id where gstatus = 0 UNION
    select '收藏了',b.id,b.title,3,a.uid,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_article_user_status a join t_article b on a.aid = b.id  where cstatus = 0 UNION
    select '关注了',b.id,b.title,3,a.uid,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_article_user_status  a join t_article b on a.aid = b.id where fstatus = 0 UNION
    select '点赞了',b.id,b.content,2,a.uid,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_inspirer_user_status a join t_inspirer b on a.iid = b.id where gstatus = 0 UNION
    select '收藏了',b.id,b.content,2,a.uid,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_inspirer_user_status a join t_inspirer b on a.iid = b.id  where cstatus = 0 UNION
    select '点赞了',b.id,b.title,1,a.uid,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_questions_user_status a join t_questions b on a.qid = b.id where gstatus = 0 UNION
    select '收藏了',b.id,b.title,1,a.uid,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_questions_user_status a join t_questions b on a.qid = b.id  where cstatus = 0 UNION
    select '关注了',b.id,b.title,1,a.uid,DATE_FORMAT(a.updatetime, '%Y.%m.%d %T') times from t_questions_user_status  a join t_questions b on a.qid = b.id where fstatus = 0 
) as a where uid = 251 order by times desc limit 100;
'''