from flask import jsonify,render_template,request
from . import userbp
from ..utils.dbtools import Db
from config import db_config
db = Db(db_config)


@userbp.route("/")
def index():
    return render_template("index.html")

@userbp.route("/questions")
def questions():
    return render_template("questions.html")


@userbp.route("/getquestions")
def getquestions():
    res = db.query("select * from t_questions limit 10;")
    # print(res)
    return jsonify(res)


@userbp.route("/questions/")
def questioncontent():
    questionid = request.args.get("questionid")
    res = db.query("select * from t_questions where id = {};".format(questionid))
    print(res)
    return jsonify(res)