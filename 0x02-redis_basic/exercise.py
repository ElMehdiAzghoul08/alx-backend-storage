#!/usr/bin/env python3

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    count_calls function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    call_history function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


def replay(method: Callable):
    """
    replay function
    """
    redis_instance = redis.Redis()
    method_name = method.__qualname__
    inputs = redis_instance.lrange(f"{method_name}:inputs", 0, -1)
    outputs = redis_instance.lrange(f"{method_name}:outputs", 0, -1)
    calls_count = redis_instance.get(method_name).decode("utf-8")

    print(f"{method_name} was called {calls_count} times:")
    for input_args, output in zip(inputs, outputs):
        input_str = input_args.decode("utf-8")
        output_str = output.decode("utf-8")
        print(f"{method_name}{input_str} -> {output_str}")


class Cache:
    """
    Cache class
    """

    def __init__(self):
        """
        __init__ function
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store function
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """
        get function
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        get_str function
        """
        data = self.get(key, fn=lambda d: d.decode("utf-8"))
        return data if data is not None else ""

    def get_int(self, key: str) -> int:
        """
        get_int function
        """
        data = self.get(key, fn=int)
        return data if data is not None else 0
