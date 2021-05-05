import functools

def memoize(function):
    function._cache = {}
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        cached = function._cache.get(key, None)
        if not cached:
            cached = function(*args, **kwargs)
            function._cache[key] = cached
        return cached
    return wrapper


