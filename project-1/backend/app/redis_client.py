import os
import redis
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

REDIS_URL = os.getenv("REDIS_URL")

redis_client = redis.from_url(
    REDIS_URL,
    decode_responses=True
)