#!/usr/bin/env python3
"""Module"""

import redis
import requests

rs = redis.Redis()
ct = 0


def get_page(url: str) -> str:
    """get_page function"""
    rs.set(f"cached:{url}", ct)
    res = requests.get(url)
    rs.incr(f"ct:{url}")
    rs.setex(f"cached:{url}", 10, rs.get(f"cached:{url}"))
    return res.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
