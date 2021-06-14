#Timing decorator function
#Author : Anders Galmén 2021

from time import time

def timer(func):
    """ Wrapper timing a function.
    Arg: a function.

    Typical usage:
    -The decorator @timer is placed before the function definition to time the function.

    Example:
    @timer
    def foo(x, y):
        print("bar")
        return x+y

    prints:
    ---- <2443140086224> starting ----
    bar
    ---- <2443140086224> finished in 0.0010004043579101562 seconds ----
    """
    def inner(*args, **kwargs):
        start_time = time()
        try:
            print(f"---- <{id(func):12}> starting ----")
            return_value = func(*args, **kwargs)
            print(f"---- <{id(func):12}> finished in {(time() - start_time)}s seconds ----")
            return return_value
        except:
            print("---- Error: no function passed")
    return inner
