# Decorators are very powerful tool in Python and every advanced Python
# programmer should know it. 

# Objectives:
# - The concept behind decorators
# - How you can write your own decorators
# - The difference between function and class decorators
# - Some typical uses cases of decorators

# @mydecorator
def dosomething():
    pass

# A decorator is a function that takes another function as argument and
# extends the behavior of this function without explicitly modifying it.
# In other words, it allows you to add new functionality to an exising function.

# In order to understand this concept, we have to know that functions in
# Python are first class objects. This means that like any other object, they
# can be defined inside another function passed as an argument to another
# function, and even returned from other function.
import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')

# print_name() # Alex, without decorator at first

# print_name = start_end_decorator(print_name)

print_name()
# Output: 
# Start
# Alex
# End

@start_end_decorator
def add5(x):
    return x + 5

result = add5(10)
print(result) # 15

print(help(add5))
# Output:
# Help on function add5 in module __main__:
#
# add5(x)
#
# None

print(add5.__name__) # add5

# Template:

# import functools

# def my_decorator(func):

#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # Do something...
#         result = func(*args, **kwargs)
#         # Do something2...
#         return result
#     return wrapper


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet('Alex')
# Output:
# Hello Alex
# Hello Alex
# Hello Alex

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result=func(*args, **kwargs)
        print(f"{func.__name__!r} returned {signature!r}")
        return result
    return wrapper

@debug
@start_end_decorator
def say_hello(name):
    greeting =  f'Hello {name}'
    print(greeting)
    return greeting

say_hello('Alex')
# Output:
# Calling say_hello('Alex')
# Start
# Hello Alex
# End
# 'say_hello' returned "'Alex'"

class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} time(s)')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print('Hello')

say_hello()
say_hello()
# Output:
# This is executed 1 times
# Hello
# This is executed 2 times
# Hello

# Some typical use cases of decorators. Examples:
# - You can implement a timer decorator to calculate the execution time of a function
# - You can use a debug decorator (like you've seen before) to print out some more info about the called function and its arguments
# - You can use a check decorator to check if the arguments fulfill some requirements and the depth of the behavior accordingly
# - You can register functions, like plug ins, with decorators
# - You can cache the return values
# - You can add information or update state generators or functions that return an object that can be iterated