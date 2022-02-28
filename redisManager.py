import redis
import json

rd = redis.StrictRedis(port=6379, db=0)

class RedisManager:

    def set(self,key, data):
        data = json.dumps(data)
        rd.set(key, data)
    def get(self,key):
        cached_data = rd.get(key)
        if not cached_data:
            return None
        
        cached_data = json.loads(cached_data)
        cached_data.decode("utf-8")
        return cached_data