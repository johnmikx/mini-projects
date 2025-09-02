# Strings: ordered, immutable, text representation
# Description: A string is an ordered and immutable collection data type
# that is used for text representation. And it is one of the most used
# data types in Python.

my_string = "Hello World" # You can use ' ', " ", """ """"
print(my_string)

my_string = 'I\'m a programmer' # You can use an escape backslash (\)
print(my_string)

my_string = "I'm a programmer" # You can use instead a double quotes for this
print(my_string)

my_string = """Hello
World""" # Used for multilines or documentation for multiple lines
print(my_string)
# Output:
# Hello
# World

my_string = """Hello \
World""" # You can use an escape bacslash(\)
print(my_string) # Continues the string in a single line
# Output: Hello World

my_string = "Hello World"
char = my_string[0]
print(char) # H

print(my_string[1]) # e
print(my_string[-1]) # d
print(my_string[-2]) # l

# my_string[0] = 'h' # TypeError: 'str' object does not support item assignment

substring = my_string[1:5]
print(substring) # ello

print(my_string[:5]) # Hello
print(my_string[:]) # Hello World
print(my_string[::1]) # Hello World
print(my_string[::2]) # HloWrd
print(my_string[::-1]) # dlroW olleH, This is reverse string

greeting = "Hello"
name = "Tom!"
sentence = greeting + " " + name
print(sentence) # Hello Tom!

for i in greeting:
    print(i)

if 'e' in greeting: # yes
    print('yes')
else:
    print('no')

if 'p' in greeting: # no
    print('yes')
else:
    print('no')

if 'ell' in greeting: # yes
    print('yes')
else:
    print('no')

my_string = '        Hello World   '
print(my_string)

my_string = "Hello World"
print(my_string.upper()) # HELLO WORLD
print(my_string.lower()) # hello world
print(my_string.startswith("")) # True
print(my_string.startswith("H")) # True
print(my_string.startswith("Hello")) # True
print(my_string.startswith("World")) # False
print(my_string.endswith("World")) # True
print(my_string.endswith("Hello")) # False
print(my_string.find('o')) # 4
print(my_string.find('lo')) # 3
print(my_string.find('pp')) # -1, does not find the string
print(my_string.count('o')) # 2
print(my_string.count('p')) # 0
print(my_string.replace('World', 'Universe')) # Hello Universe
print(my_string.replace('Worrrld', 'Universe')) # Hello World, still prints the original strings

my_string = 'how are you doing'
my_list = my_string.split()
print(my_list) # ['how', 'are', 'you', 'doing']
print(my_string.split(" ")) # ['how', 'are', 'you', 'doing']

my_string = 'how,are,you,doing'
my_list = my_string.split(",")
print(my_list) # ['how', 'are', 'you', 'doing']

new_string = ''.join(my_list)
print(new_string) # howareyoudoing

print(" ".join(my_list)) # how are you doing

from timeit import default_timer as timer

my_list = ['a'] * 6
print(my_list) # ['a', 'a', 'a', 'a', 'a', 'a']

# bad
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(stop-start) # 1.1299969628453255e-05 second
print(my_string) # aaaaaa

# good
start = timer()
my_string = ''.join(my_list)
start = timer()
print(stop-start) # -0.0004065000102855265 second
print(my_string) # aaaaaa

# % (very-old formatting style), .format(), f-Strings
var = "Tom"
my_string = "the variable is %s" % var # %s for strings
print(my_string) # the variable is Tom

var = 3
my_string = "the variable is %d" % var # %d for integers
print(my_string) # the variable is 3

var = 3.14
my_string = "the variable is %d" % var
print(my_string) # the variable is 3

var = 2.71828
my_string = "the variable is %f" % var # %f for floating-point
print(my_string) # the variable is 2.718280

var = 2.71828
my_string = "the variable is %.2f" % var # %f for floating-point with specified rounded decimal points
print(my_string) # the variable is 2.72

var = 2.71828
my_string = "the variable is {}".format(var)
print(my_string) # the variable is 2.71828

var = 2.71828
my_string = "the variable is {:.2f}".format(var)
print(my_string) # the variable is 2.72

var = 2.71828
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var, var2)
print(my_string) # the variable is 2.72 and 6

var = 2.71828
var2 = 6
my_string = f"the variable is {var} and {var2}"
print(my_string) # the variable is 2.71828 and 6

var = 2.71828
var2 = 6
my_string = f"the variable is {var:.2f} and {var2}"
print(my_string) # the variable is 2.72 and 6

var = 2.71828
var2 = 6
my_string = f"the variable is {var*2} and {var2}"
print(my_string) # the variable is 5.43656 and 6