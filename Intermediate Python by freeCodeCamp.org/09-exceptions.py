# Errors and Exceptions
# Description: A Python program terminates as soon as it encounters an
# Error, and an Error can be either a SyntaxError or an ExceptionError.

# What are the difference between a SyntaxError and an Exception?
# What are the most common built-in Exceptions?
# How can we raise and handle Exceptions?
# How can we define our own Exception?

# A SyntaxError occurs when the parsers detects a syntactically incorrect
# statement.

# a = 5 print(a) # SyntaxError: invalid syntax

a = 5
# print(a)) # SyntaxError: unmatched ')'

# a = 5 + '10' # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# import somemodule # ModuleNotFoundError: No module named 'somemodule'

a = 5
# b = c # NameError: name 'c' is not defined

# f = open('somefile.txt') # FileNotFoundError: [Errno 2] No such file or directory: 'somefile.txt'

a = [1, 2, 3]
# a.remove(4) # ValueError: list.remove(x): x not in list
# a[4] # IndexError: list index out of range

my_dict = {'name':'Max'}
# my_dict['age'] # KeyError: 'age'

x = -5
# if x < 0:
    # raise Exception('x should be positive') # Exception: x should be positive

x = 5
if x < 0:
    raise Exception('x should be positive') # No Exception will be raised

x = -5
# assert(x >= 0) # AssertionError
# assert(x >= 0), 'x is not positive' # AssertionError: x is not positive

# a = 5 / 0 # ZeroDivisionError: division by zero

try:
    a = 5 / 0
except:
    print('an error occured')

try:
    a = 5 / 0
except Exception as e:
    print(e) # division by zero

try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e) # unsupported operand type(s) for +: 'float' and 'str'

try:
    a = 5 / 1
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine') # everything is fine
finally: # This runs always no matter if there was an Exception or not
    print('cleaning up...') # cleaning up...

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')

# test_value(200) # ValueTooHighError: value is too high

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small,', x)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e) # value is too high
except ValueTooSmallError as e:
    print(e.message, e.value) # value is too small, 1