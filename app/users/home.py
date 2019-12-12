from flask import jsonify,render_template,request
from . import userbp
from ..utils.dbtools import Db
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
    return jsonify(data)

@userbp.route("/getcoures")
def getcoures():
    '''
    教程
    '''
    res = db.query("select id,title,content from t_coures where status = 0 limit 4;")
    data = {
        "status":200,
        "data":res,
        "msg":"查询成功！"
    }
    return jsonify(data)

@userbp.route("/getquestions")
def getquestions():
    '''
    讨论
    '''
    num = request.args.get("num")
    if num is None:
        num = 6
    res = db.query("select id,title,content,tags from t_questions where status = 0 limit {};".format(num))
    data = {
        "status":200,
        "data":res,
        "msg":"查询成功！"
    }
    return jsonify(data)

@userbp.route("/getarticle")
def getarticle():
    '''
    文章
    '''
    num = request.args.get("num")
    if num is None:
        num = 6
    res = db.query("select id,title,content,tags from t_article where status = 0  limit {};".format(num))
    data = {
        "status":200,
        "data":res,
        "msg":"查询成功！"
    }
    return jsonify(data)

@userbp.route("/getinspirer")
def getinspirer():
    '''
    灵感
    '''
    num = request.args.get("num")
    if num is None:
        num = 6
    res = db.query("select id,content from t_inspirer where status = 0  limit {};".format(num))
    data = {
        "status":200,
        "data":res,
        "msg":"查询成功！"
    }
    return jsonify(data)

@userbp.route("/gethighusers")
def gethighusers():
    '''
    活跃用户
    '''
    num = request.args.get("num")
    if num is None:
        num = 15
    res = db.query("select id,nickname,headpic from t_user where status = 0 limit {};".format(num))
    data = {
        "status":200,
        "data":res,
        "msg":"查询成功！"
    }
    return jsonify(data)

