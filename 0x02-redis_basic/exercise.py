#!/usr/bin/env python3
"""
Module to define Cache class using Redis
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps

def count_calls(method: Callable) -> Callable:
    '''
    Counts the number of times a method is called.
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
        Wrapper function.
        '''
        method_name = method.__qualname__
        self._redis.incr(method_name)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a particular function.
    """
    method_name = method.__qualname__
    inputs_key = method_name + ":inputs"
    outputs_key = method_name + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper for decorator functionality."""
        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))
        return result

    return wrapper

def replay(method: Callable) -> None:
    """
    Replays the history of a function
    Args:
        method: The function to be decorated
    Returns:
        None
    """
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode('utf-8'),
                                     o.decode('utf-8')))

class Cache:
    """
    Cache class.
    """
    def __init__(self):
        """
        Initialize the cache.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the cache.
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str,
            transform_fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Get data from the cache.
        """
        value = self._redis.get(key)
        if transform_fn:
            value = transform_fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Get a string from the cache.
        """
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """
        Get an int from the cache.
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except (ValueError, TypeError):
            value = 0
        return value
