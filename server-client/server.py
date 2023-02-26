import redis

with redis.Redis() as redis.server:
redis_server = redis.Redis()

redis_server.close()