import os
import hashlib
import json
from pymemcache.client.base import Client
from utilities.logging_config import get_logger

logger = get_logger(__name__)


def create_connection():
    """
    Create and return Memcache connection
    """
    host = os.getenv("MEMCACHED_HOST", "memcached")
    port = os.getenv("MEMCACHED_PORT", 11211)

    return Client((host, int(port)), connect_timeout=2, timeout=2)


def set_cache(key, value, expire=600):
    try:
        client = create_connection()
        safe_key = hashlib.sha256(key.encode()).hexdigest()
        client.set(safe_key, json.dumps(value), expire)
        logger.info(f"{key} added in Memcache")
    except Exception as e:
        logger.exception(f"Error while adding {key} in memcache. Error {e}")
    finally:
        client.close()
        logger.info("Closing Memcache Connection.")


def get_cache(key):
    try:
        client = create_connection()
        safe_key = hashlib.sha256(key.encode()).hexdigest()
        data = client.get(safe_key)
        return json.loads(data.decode())
    except Exception as e:
        logger.info(f"Failed to get cache for key {key}. Error : {e}")
    finally:
        client.close()
        logger.info("Closing Memcache connection.")


def clear_cache(key):
    try:
        client = create_connection()
        safe_key = hashlib.sha256(key.encode()).hexdigest()
        client.delete(safe_key)
        logger.info("Cache cleared from memcache.")
    except Exception as e:
        logger.exception(f"Failed to clear cache. Error : {e}")
    finally:
        client.close()
        logger.info("Closing Memcache connection.")
