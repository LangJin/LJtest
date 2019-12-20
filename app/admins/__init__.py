# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Blueprint


adminbp = Blueprint("admin", __name__)

from . import admin