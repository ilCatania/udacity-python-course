import inspect

def bind_args(function, *args, **kwargs):
    return inspect.signature(function).bind(*args, **kwargs).arguments

