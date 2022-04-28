# publisher.py
import redis
import random
import time, json

r = redis.Redis(host='local host', port=6379, db=0)

temp = 0.0

while True:
    temp = random.uniform(10.0, 40.0)
    string_temp = str(temp)
    r.publish('canal-1', string_temp)
    time.sleep(5)
    