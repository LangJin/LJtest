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
                    session["admininfo"] = {"token":token,"uid":res[0]["id"]}
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


# 教程的增删改查
# 灵感的搜索、删除
# 文章的搜索删除
# 问题的搜索删除
# 用户的搜索删除
@adminbp.route("/userlist",methods=["get"])
def userlist():
    headrsmsg = checkContentType(request)
    if headrsmsg != True:
        return setcors(msg=headrsmsg)
    pagenum = int(request.args.get("pagenum"))
    endnum = 10
    if pagenum == 1:
        startnum = 0
    else:
        startnum = (pagenum-1)*10
    loginstatus = checkloginstatus(session,token)
    if loginstatus is True:
        allusernum = db.query("select count(*) usernum  from t_user where status = 0 ;")
        res = db.query("select * from t_user where status = 0 limit {},{};".format(startnum,endnum))
        data = {
            "userlist":res,
            "usernum":allusernum[0].get("usernum")
        }
        return setcors(data=data,status=200)
    else:
        return setcors(msg=loginstatus)
