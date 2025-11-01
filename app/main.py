from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_data = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            for item in list(args) + list(kwargs.items()):
                hash(item)
        except TypeError:
            return func(*args, **kwargs)

        key = (args, tuple(sorted(kwargs.items())))

        if key not in cache_data:
            print("Calculating new result")
            cache_data[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return cache_data[key]
    return wrapper
