# publisher.py
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.publish('canal-1', 'dato del canal 1')
