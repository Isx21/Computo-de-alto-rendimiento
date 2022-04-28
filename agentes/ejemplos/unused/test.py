import redis
r=redis.Redis("localhost", port=6379, db=0)
r.set("test_resultado", "trabajando")

