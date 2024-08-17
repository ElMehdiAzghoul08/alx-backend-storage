#!/usr/bin/env python3
"""Module"""

import redis
import requests
from functools import wraps
from typing import Callable

rs = redis.Redis()


def get_page(url: str) -> str:
    """get_page function"""
    rs.incr(f"count:{url}")

    cached_response = rs.get(f"cached:{url}")
    if cached_response:
        return cached_response.decode('utf-8')

    res = requests.get(url)

    rs.setex(f"cached:{url}", 10, res.text)

    return res.text


if __name__ == "__main__":
    print(get_page('http://slowwly.robertomurray.co.uk'))
