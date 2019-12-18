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
    res = db.query("select id,title,content,imghost from t_title_img;")
    data = {
        "status":200,
        "data":res,
        "msg":"查询成功！"
    }
    return setcors(data)

@userbp.route("/getcoures")
def getcoures():
    '''
    教程
    '''
    num = request.args.get("num")
    if num is None:
        num = '4'
    nummsg = is_number(num)
    if nummsg == True:
        res = db.query("select id,title,content,ximg from t_coures where status = 0 limit {};".format(num))
        data = {
            "status":200,
            "data":res,
            "msg":"查询成功！"
        }
    else:
        data = {
            "status":401,
            "data":None,
            "msg":"num只能是数字！"
        }   
    return setcors(data)

@userbp.route("/get/coure")
def getcourecid():
    '''
    获取具体的教程内容
    '''
    cid = request.args.get("cid")
    nummsg = is_number(cid)
    if nummsg == True:
        res = db.query("select id,title,content,ximg,uid from t_coures where status = 0 and id = {};".format(cid))
        data = {
            "status":200,
            "data":res,
            "msg":"查询成功！"
        }
    else:
        data = {
            "status":401,
            "data":None,
            "msg":"id只能是数字！且不能为空"
        }   
    return setcors(data)


@userbp.route("/getquestions")
def getquestions():
    '''
    讨论
    '''
    num = request.args.get("num")
    if num is None:
        num = '6'
    nummsg = is_number(num)
    if nummsg == True:
        res = db.query("select id,title,content,tags,ximg,uid from t_questions where status = 0 limit {};".format(num))
        data = {
            "status":200,
            "data":res,
            "msg":"查询成功！"
        }
    else:
        data = {
            "status":401,
            "data":None,
            "msg":"num只能是数字！"
        }      
    return setcors(data)


@userbp.route("/get/question")
def getquestionqid():
    '''
    获取具体的问题内容
    '''
    qid = request.args.get("qid")
    nummsg = is_number(qid)
    if nummsg == True:
        res = db.query("select id,title,content,tags,ximg,uid from t_questions where status = 0 and id = {};".format(qid))
        data = {
            "status":200,
            "data":res,
            "msg":"查询成功！"
        }
    else:
        data = {
            "status":401,
            "data":None,
            "msg":"qid只能是数字！且不能为空！"
        }      
    return setcors(data)


@userbp.route("/getarticle")
def getarticle():
    '''
    文章
    '''
    num = request.args.get("num")
    if num is None:
        num = '6'
    nummsg = is_number(num)
    if nummsg == True:
        res = db.query("select id,title,content,tags,ximg,uid from t_article where status = 0  limit {};".format(num))
        data = {
            "status":200,
            "data":res,
            "msg":"查询成功！"
        }
    else:
        data = {
            "status":401,
            "data":None,
            "msg":"num只能是数字！"
        }  
    return setcors(data)


@userbp.route("/get/article")
def getarticleaid():
    '''
    获取具体的文章内容文章
    '''
    aid = request.args.get("aid")
    nummsg = is_number(aid)
    if nummsg == True:
        res = db.query("select id,title,content,tags,ximg,uid from t_article where status = 0  and id = {};".format(aid))
        data = {
            "status":200,
            "data":res,
            "msg":"查询成功！"
        }
    else:
        data = {
            "status":401,
            "data":None,
            "msg":"aid只能是数字！,且不能为空"
        }  
    return setcors(data)


@userbp.route("/getinspirer")
def getinspirer():
    '''
    灵感
    '''
    num = request.args.get("num")
    if num is None:
        num = '6'
    nummsg = is_number(num)
    if nummsg == True:
        res = db.query("select id,content,ximg,uid from t_inspirer where status = 0  limit {};".format(num))
        data = {
            "status":200,
            "data":res,
            "msg":"查询成功！"
        }
    else:
        data = {
            "status":401,
            "data":None,
            "msg":"num只能是数字！"
        }  
    return setcors(data)


@userbp.route("/get/inspirer")
def getinspireriid():
    '''
    灵感具体内容
    '''
    iid = request.args.get("iid")
    nummsg = is_number(iid)
    if nummsg == True:
        res = db.query("select id,content,ximg,uid from t_inspirer where status = 0  and id = {};".format(iid))
        data = {
            "status":200,
            "data":res,
            "msg":"查询成功！"
        }
    else:
        data = {
            "status":401,
            "data":None,
            "msg":nummsg
        }  
    return setcors(data)


@userbp.route("/gethighusers")
def gethighusers():
    '''
    活跃用户
    '''
    num = request.args.get("num")
    if num is None:
        num = '15'
    nummsg = is_number(num)
    if nummsg == True:
        res = db.query("select id,nickname,headpic from t_user where status = 0 limit {};".format(num))
        data = {
            "status":200,
            "data":res,
            "msg":"查询成功！"
        }
    else:
        data = {
            "status":401,
            "data":None,
            "msg":"num只能是数字！"
        }  
    return setcors(data)


@userbp.route("/get/userinfo")
def getuserinfo():
    '''
    用户主页
    '''
    uid = request.args.get("uid")
    nummsg = is_number(uid)
    if nummsg == True:
        res = db.query("select * from t_user where status = 0 and id = {};".format(uid))
        data = {
            "status":200,
            "data":res,
            "msg":"查询成功！"
        }
    else:
        data = {
            "status":401,
            "data":None,
            "msg":nummsg
        }  
    return setcors(data)