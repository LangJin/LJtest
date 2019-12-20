# -*- coding:utf-8 -*-
__author__ = 'LangJin'

from flask import request,session,make_response
from . import adminbp
from ..utils.dbtools import Db
from config import db_config
from ..utils.othertools import checkuserinfo,create_token,encryption,setcors,checkloginstatus,checkContentType,is_number,checkvalueisNone
# from werkzeug import secure_filename


db = Db(db_config)



@adminbp.route("/adminlogin",methods=["post"])
def adminlogin():
    '''
    管理员登录接口\n
    获取json格式的数据进行处理
    '''
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    else:
        userinfo = request.get_json()
        username = userinfo.get("username")
        password = userinfo.get("password")
        userregmsg = checkuserinfo(username,password)
        if userregmsg is True:
            sql = "select * from t_admin where status = 0 and username = '{}'".format(username)
            res = db.query(sql)
            if len(res) != 1:
                return setcors(msg="账号不存在或者账号异常")
            else:
                # password = encryption(username,password,"admin")
                if password == res[0].get("password"):
                    token = create_token()
                    session.clear()
                    session["userinfo"] = {"token":token,"uid":res[0]["id"]}
                    userinfo = {
                        "nickname":res[0]["nickname"],
                        "uid":res[0]["id"],
                        "headpic":res[0]["headpic"]
                    }
                    data = {}
                    data["userinfo"] = userinfo
                    data["token"] = token
                    return setcors(msg="登录成功！",data=data,status=200)
                else:
                    return setcors(msg="密码错误")
        else:
            return setcors(msg=userregmsg)


