from flask import jsonify,render_template,request
from . import userbp
from ..utils.dbtools import Db
from config import db_config
db = Db(db_config)


@userbp.route("/get_title_img")
def get_title_img():
    res = db.query("select id,title,content,imghost from t_title_img;")
    return jsonify(res)

@userbp.route("/getcoures")
def getcoures():
    res = db.query("select id,title,content from t_coures limit 4;")
    return jsonify(res)
