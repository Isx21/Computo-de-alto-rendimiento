# publisher2.py
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.publish('canal-2', 'dato del canal 2')
