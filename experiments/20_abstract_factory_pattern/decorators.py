# -*- coding: utf-8 -*-
# decorators.py


# def class_decoration(func_decoration):
#     def inner(cls):
#         for attr_name in dir(cls):
#             attr_value = getattr(cls, attr_name)
#             if hasattr(attr_value, '__call__'):  # check if attr is a function
#                 setattr(cls, attr_name, func_decoration(attr_value))
#         return cls
#     return inner


def repeat(times):
    def inner(func):
        def wrapper(*args, **kwargs):
            passed, failed = 0, 0
            return_value = func(*args, **kwargs)
            for i in range(times):
                try:
                    return_value = func(*args, **kwargs)
                    passed += 1
                except Exception:
                    failed += 1
            if failed > 0:
                print('{.__name__} FAILED {} times out of {}'.format(func, failed, times))
            if passed > 0:
                print('{.__name__} PASS {} times out of {} \n'.format(func, passed, times))
            return return_value
        return wrapper
    return inner



