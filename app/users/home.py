from flask import jsonify,render_template
from . import userbp



@userbp.route("/")
def index():
    return "浪晋的测试小讲堂"