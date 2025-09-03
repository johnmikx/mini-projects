"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference?)
"""

"""
Parameters are the variables that are defined or used inside parenthesis
where defining a function. Arguments the values passed for these parameters
while calling a function.
"""

def print_name(name): # --> `name` here is a parameter
    print(name)

print_name('Alex') # --> 'Alex' is an argument

def foo(a, b , c): 
    print(a, b, c)

foo(1, 2, 3) # --> 1, 2, 3 are positional arguments
foo(a=1, b=2, c=3) # --> a=1, b=2, c=3 are keyword arguments
foo(c=1, b=2, a=3) # The order doesn't matter for keyword arguments
foo(1, b=2, c=3) # --> can use both positional and keyword arguments
# foo(1, b=2, 3) # SyntaxError: positional argument follows keyword argument
# Cannot used positional argument after keyword argument

"""
Sometimes it's better to use keyword arguments because it makes it more clear
what they present. Or we can rearrange the arguments in a way that makes the
most readable.
"""

def foo(a, b , c, d=4): 
    print(a, b, c, d)

foo(1, 2, 3) # 1 2 3 4 --> 4 is a default argument here
foo(1, 2, 3, 7) # 1, 2, 3, 7

# Default arguments must be at the end of your function parameters.

# def foo(a, b=2 , c, d=4): # SyntaxError: parameter without a default follows parameter with a default

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
"""
If you mark a parameter with one (*) asterisk, then you can pass any number
of positional arguments to your function. If you mark a parameter with two
(**) asterisk, then you can pass any number of keyword arguments to this
function. 
"""

foo(1, 2, 3, 4, 5, six=6, seven=7)
foo(1, 2, six=6, seven=7)
foo(1, 2, 3, 4)

# Forced keyword arguments
def foo(a, b, *, c, d): # Every parameter after asterisk (*) must be a keyword argument
    print(a, b, c, d)

# foo(1, 2, 3, 4) # TypeError: foo() takes 2 positional arguments but 4 were given
foo(1, 2, c=3, d=4) # 1, 2, 3, 4

def foo(*args, last): # Each parameter after must be a keyword parameters
    for arg in args:
        print(arg)
    print(last)

# foo(1, 2, 3) # TypeError: foo() missing 1 required keyword-only argument: 'last'
foo(1, 2, 3, last=100)

# Unpacking into function arguments
def foo(a, b, c):
    print(a, b, c)

my_list = [0, 1, 2] # or my_list = (0, 1, 2)
foo(*my_list) # 0 1 2

"""
The length of your container [0, 1, 2] must match the number of parameters
here (a, b, c).
"""

my_list = (0, 1, 2, 3)
# foo(*my_list) # TypeError: foo() takes 3 positional arguments but 4 were given

my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict) # 1 2 3

# Local vs. Global Variables
def foo():
    x = number
    print('number inside function:', x) # --> Local Variable

number = 0 # --> Global Variable

foo() # number inside function: 0

def foo():
    global number
    x = number
    number = 3
    print('number inside function:', x)

number = 0
foo() # number inside function: 0
print(number) # 3

def foo():
    global number
    number = 3

number = 0
foo()
print(number) # 3

# Parameter passing
"""
Maybe you've heard, call by value or call by reference. And in Python, it's
a little bit different. It uses a mechanism which is known as call by object
or call by object reference. There are two rules that must be considered:

- Parameters are passed? or
- Parameters passed in? (It is actually a reference to an object but the reference by value)

There is a difference between mutable and immutable data types.

This basically means that mutable objects like lists or dictionaries can
be changed within a method. But if you rebind the reference in the method,
then the outer reference will still point to the original object and is
not changed.

Immutable objects like integers or strings cannot be changed within a method.
But immutable objects contained within a mutable object can be reassigned
within a method.
"""

def foo(x):
    x = 5

var = 10 # immutable type, it cannot be changed
foo(var)
print(var) # 10

def foo(a_list):
    a_list.append(4)

my_list = [1, 2, 3] # immutable objects contained within a mutable object
foo(my_list) # # it can be modified within a function
print(my_list) # [1, 2, 3, 4]

def foo(a_list):
    a_list.append(4)
    a_list[0] = -100

my_list = [1, 2, 3] # immutable objects contained within a mutable object
foo(my_list) 
print(my_list) # [-100, 2, 3, 4]

def foo(a_list):
    a_list = [200, 300, 400] # not possible if you rebind the reference, and it becomes the new local variable
    a_list.append(4)
    a_list[0] = -100

my_list = [1, 2, 3]
foo(my_list) 
print(my_list) # [1, 2, 3]

def foo(a_list):
    a_list += [200, 300, 400] # this is possible

my_list = [1, 2, 3]
foo(my_list) 
print(my_list) # [1, 2, 3, 200, 300, 400]

def foo(a_list):
    a_list = a_list + [200, 300, 400] # this is not possible

my_list = [1, 2, 3]
foo(my_list) 
print(my_list) # [1, 2, 3], returns into original

"""
Be careful with this slight difference!
"""