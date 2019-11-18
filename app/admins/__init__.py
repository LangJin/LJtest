# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Blueprint

adminbp = Blueprint("adminbp", __name__,url_prefix="/admin")

from . import admin