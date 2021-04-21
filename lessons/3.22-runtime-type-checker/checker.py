import functools
import helper


def check_types(severity=1):
    if severity == 0:
        return lambda function: function
    if severity == 1:
        message = print
    else:
        def message(msg):
            raise TypeError(msg)
    def checker(function):
        ann = function.__annotations__
        if not ann:
            return function
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            arg_types = helper.bind_args(function, *args, **kwargs)
            for arg, arg_value in arg_types.items():
                expected_type = ann.get(arg, None)
                if expected_type and not isinstance(arg_value, expected_type):
                    message(f"Argument {arg} expected of type: {expected_type} but found: {arg_value}")
            ret = function(*args, **kwargs)
            expected_return_type = ann.get("return", None)
            if expected_return_type and not isinstance(ret, expected_return_type):
                message(f"Return value expected of type: {expected_type} but found: {arg_value}")
            return(ret)
        return wrapper
    return checker

