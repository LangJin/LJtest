# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Blueprint

userbp = Blueprint("user", __name__)

from . import home,user