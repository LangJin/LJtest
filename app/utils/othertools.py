# -*- coding:utf-8 -*-
__author__ = 'LangJin'

import os, hashlib



def create_token():
    '''
    生成登陆后的token，格式如下：\n
    "eca7f38788d4764959919b46c61005038cf37f68"
    '''
    return hashlib.sha1(os.urandom(64)).hexdigest()

def encryption(username,password,role):
    '''
    说明：密码的加密算法,role是角色\n
    用法:encryption("用户名","明文密码","user")
    '''
    md5 = hashlib.md5()
    md5.update(password.encode("utf8")+username.encode("utf8")+keys.get(role).encode("utf8"))
    password = md5.hexdigest()
    return password

def checkusername(username):
    '''
    检查账号是否满足用户需求
    '''
    if len(username) >= 6 and len(username) <= 12:
        for i in username:
            if i not in "0123456789qazwsxedcrfvtgbyhnujmikolp":
                return "账号仅能由数字和字母组成！"
        return True
    else:
        return "账号长度必须大于等于6位，并且小于等于12位"


def checkpasswd(password):
    '''
    检查密码是否符合规范
    '''
    if len(password) >= 8 and len(password) <= 16:
        return True
    else:
        return "账号长度必须大于等于6位，并且小于等于12位"