import redis
import json
from typing import Any

# Connect to Redis (adjust URL in .env or settings)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

# Cache result with a key
def set_cache(key: str, value: Any, ttl: int = 3600):
    redis_client.setex(key, ttl, json.dumps(value))

# Get cache result for a key
def get_cache(key: str) -> Any:
    cached_value = redis_client.get(key)
    if cached_value:
        return json.loads(cached_value)
    return None
