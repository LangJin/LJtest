# -*- coding:utf-8 -*-
__author__ = 'LangJin'
import pymysql
from config import db_config

def query(sql=''):
    '''
    用法：query('select * from t_user;')\n
    说明：查询数据库工具,返回查询结果
    '''
    db = pymysql.connect(**db_config)
    cursor = db.cursor()
    try:
        cursor.execute(sql)  # 执行sql语句
        # 获得列名
        descs = []
        for desc in cursor.description:
            descs.append(desc[0])

        # 构造键值对{"列名":数据}
        results = []
        for res in cursor.fetchall():
            # (906985036, 'zhangsan', 'a11313', None, None)
            row = {}
            for i in range(len(descs)):
                row[descs[i]] = res[i]
            results.append(row)
    except Exception as e:
        raise e
    finally:
        cursor.close()
        db.close()  # 关闭连接
        return results


def commit(sql=''):
    '''
    用法：commit('insert into t_user (id,username) values (1,'张三');')\n
    说明：更改数据库工具，支持插入、修改、删除
    '''
    res = True
    db = pymysql.connect(**db_config)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        res = False
    finally:
        cursor.close()
        db.close()
        return res

