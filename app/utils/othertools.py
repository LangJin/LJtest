# -*- coding:utf-8 -*-
__author__ = 'LangJin'

import os, hashlib
from config import keys


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


