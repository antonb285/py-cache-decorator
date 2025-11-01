from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_data = {}
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Callable:
        items = args
        if items not in cache_data:
            print("Calculating new result")
            cache_data[items] = func(*args, **kwargs)
            return cache_data[items]
        else:
            print("Getting from cache")
            return cache_data[items]
    return wrapper

