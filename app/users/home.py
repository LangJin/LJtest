from flask import jsonify,render_template
from . import userbp
from ..utils.mysqltools import query



@userbp.route("/home/getbigimg")
def getbigimg():
    sql = 'select * from t_home_bigimg;'
    res = query(sql)

    data = res
    return jsonify(data)


@userbp.route("/")
def index():
    return render_template('index.html')


@userbp.route("/login")
def getloginhtml():
    return render_template('login.html')