from redis import StrictRedis
from config import redis_config
import json

class RedisDb:
    '''
    Redis的工具类
    '''
    def __init__(self,db_config):
        self.db_config = db_config

    def setredisvalue(self,token,value):
        '''
        设置用户缓存，并返回结果
        '''
        redis = StrictRedis(**self.db_config)
        if type(value) is dict:
            value = json.dumps(value)
        redis.set(token, value)
        res = redis.get(token)
        res = json.loads(res)
        return res
    
    def getredisvalue(self,token):
        '''
        根据token读取用户缓存
        '''
        redis = StrictRedis(**self.db_config)
        res = redis.get(token)
        try:
            res = json.loads(res)
            return res
        except:
            return res


redisdb = RedisDb(redis_config) 
redisdb.setredisvalue("asdhas",{"a":"1"})