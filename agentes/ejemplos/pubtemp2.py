# publisher.py
import redis
import random
import time, json

r = redis.Redis(host='localhost', port=6379, db=0)

temp = 0.0

while True:
	temp = random.uniform(10.0, 40.0)
	lum = random.uniform(10.0, 40.0)
	hum = random.uniform(10.0, 40.0)
	json_datos = json.dumps({"id":"temp","valor": temp, "hum": hum, "lum": lum})
	print(json_datos)
	r.publish('canal-1', json_datos)
	time.sleep(5)
