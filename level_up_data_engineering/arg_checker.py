from functools import wraps


def arg_checker(*arg_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            if len(args) != len(arg_types):
                raise TypeError(f'Function {func.__name__} takes {len(arg_types)} positional arguments but {len(arg_types)} given ')
            for arg, arg_types in zip(args,arg_types):
                if not isinstance(arg,arg_types):
                    raise TypeError(f'Function {func.__name__} expected positional arguments of type {arg_types} but got {type(arg)} instead')
            return func(*args)
        return wrapper
    return decorator