import os
import base64
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
        safe_key = base64.urlsafe_b64encode(key.encode()).decode()
        client.set(safe_key, value, expire)
        logger.info(f"{key} added in Memcache")
    except Exception as e:
        logger.exception(f"Error while adding {key} in memcache. Error {e}")
    finally:
        client.close()
        logger.info("Closing Memcache Connection.")


def get_cache(key):
    try:
        client = create_connection()
        safe_key = base64.urlsafe_b64encode(key.encode()).decode()
        client.get(safe_key)
    except Exception as e:
        logger.info(f"Failed to get cache for key {key}. Error : {e}")
    finally:
        client.close()
        logger.info("Closing Memcache connection.")
