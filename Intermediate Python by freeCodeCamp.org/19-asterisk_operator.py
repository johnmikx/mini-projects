"""
The Asterisk (*) can be used for multiple different cases like multiplication
and power operations, the creation of lists or tuples, with repeated elements,
for *args, **kwargs, and keyword only parameters, for unpacking lists, tuples,
or dictionaries into function arguments, for unpacking containers, and for
merging containers into a list or merging two dictionaries.
"""

result = 5 * 7
print(result) # 35

result = 5 ** 7
print(result) # 78125

zeros = [0] * 10
print(zeros) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

zeros = [0, 1] * 5
print(zeros) # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

zeros = (0, 1) * 3
print(zeros) # (0, 1, 0, 1, 0, 1)

letters = "AB" * 2
print(letters) # ABAB

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)

    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)

# Unpacking list[]
def foo(a, b, c):
    print(a, b, c)

my_list = [0, 1, 2]
foo(*my_list) # 0 1 2, like *args

# Unpacking  tuple()
def foo(a, b, c):
    print(a, b, c)

my_tuple = (0, 1, 2)
foo(*my_tuple) # 0 1 2, like *args

# Unpacking dictionary{}
def foo(a, b, c):
    print(a, b, c)

my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict) # 1 2 3, like **kwargs

# *beginning
numbers = [1, 2, 3, 4, 5, 6]

*beginning, last = numbers
print(beginning) # [1, 2, 3, 4, 5]
print(last) # 6

# *last
numbers = [-1, 0, 1, 2, 3, 4, 5]

beginning, *last = numbers
print(beginning) # -1
print(last) # [0, 1, 2, 3, 4, 5]

# *middle
numbers = [-3, -2, -1, 0, 1, 2, 3]

beginning, *middle, last = numbers
print(beginning) # -3
print(middle) # [-2, -1, 0, 1, 2]
print(last) # 3

# *middle with secondlast
numbers = [-3, -2, -1, 0, 1, 2, 3]

beginning, *middle, secondlast, last = numbers
print(beginning) # -3
print(middle) # [-2, -1, 0, 1]
print(secondlast) # 2
print(last) # 3

my_tuple = (1, 2, 3)
my_list = [4, 5, 6]

new_list = [*my_tuple, *my_list]
print(new_list) # [1, 2, 3, 4, 5, 6], new merged list

my_tuple = (1, 2, 3)
my_set = [4, 5, 6]

new_list = [*my_tuple, *my_set]
print(new_list) # [1, 2, 3, 4, 5, 6], new merged list | this works for set

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}

my_dict = {**dict_a, **dict_b}
print(my_dict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}, new merged dictionary