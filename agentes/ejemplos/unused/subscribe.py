# subscriber.py
import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0)

p = r.pubsub()

p.subscribe("canal-1", "canal-2")

while True:
  message = p.get_message()
  if message:
    print(message)
  time.sleep(0.01)
