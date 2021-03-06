# -*- coding:utf-8 -*-
from flask import render_template,Blueprint
# from app import bp
errorbp = Blueprint("errorbp",__name__)

# @errorbp.app_errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# @errorbp.app_errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500


@errorbp.app_errorhandler(404)
def page_not_found(e):
    return "404", 404

@errorbp.app_errorhandler(500)
def internal_server_error(e):
    return "500", 500