#!/usr/bin/env python3

import redis
import requests
from functools import wraps
from typing import Callable


def cache_and_track(expiration_time: int = 10) -> Callable:
    """
    cache_and_track function
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            """
            wrapper function
            """
            redis_client = redis.Redis()
            count_key = f"count:{url}"
            content_key = f"content:{url}"

            redis_client.incr(count_key)

            cached_content = redis_client.get(content_key)
            if cached_content:
                return cached_content.decode('utf-8')

            result = func(url)

            redis_client.setex(content_key, expiration_time, result)

            return result
        return wrapper
    return decorator


@cache_and_track()
def get_page(url: str) -> str:
    """
    get_page function
    """
    response = requests.get(url)
    return response.text
