from flask import render_template,request
from . import userbp
from ..utils.dbtools import Db
from ..utils.othertools import setcors
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
    if num in '1234567890':
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


@userbp.route("/getquestions")
def getquestions():
    '''
    讨论
    '''
    num = request.args.get("num")
    if num is None:
        num = '6'
    if num in '1234567890':
        res = db.query("select id,title,content,tags,ximg from t_questions where status = 0 limit {};".format(num))
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

@userbp.route("/getarticle")
def getarticle():
    '''
    文章
    '''
    num = request.args.get("num")
    if num is None:
        num = '6'
    if num in "1234567890":
        res = db.query("select id,title,content,tags,ximg from t_article where status = 0  limit {};".format(num))
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

@userbp.route("/getinspirer")
def getinspirer():
    '''
    灵感
    '''
    num = request.args.get("num")
    if num is None:
        num = '6'
    if num in '1234567890':
        res = db.query("select id,content,ximg from t_inspirer where status = 0  limit {};".format(num))
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

@userbp.route("/gethighusers")
def gethighusers():
    '''
    活跃用户
    '''
    num = request.args.get("num")
    if num is None:
        num = '15'
    if num in '1234567890':
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
