# Tuple: ordered, immutable, allows duplicate elements
# Description: A tuple is a collection data type that is
# ordered and immutable. It is similar to a list with a main
# difference to the tuple cannot be changed after its
# creation. A tuple is often used for objects that belong
# together.

mytuple = ('Max', 28, 'Boston')
print(mytuple)

mytuple = 'Max', 28, 'Boston' # Parenthesis is optional
print(mytuple)

mytuple2 = ('Max')
print(mytuple2) # Not recognized as tuple
print(type(mytuple2)) # Recognized as string

mytuple3 = ('Max',)
print(mytuple3) # Recognized as tuple
print(type(mytuple3)) # Putting a comma tho it might look strange

mytuple4 = tuple(['Max', 28, 'Boston'])
print(mytuple4)

print(mytuple[0])
print(mytuple[1])
print(mytuple[2])
print(mytuple[-1])
print(mytuple[-2])
print(mytuple[-3])

# mytuple[0] = 'Tim' # TypeError: 'tuple' object does not support item assignment
# Since tuple is immutable

for x in mytuple:
    print(x)

if 'Max' in mytuple:
    print('yes')
else:
    print('no')

if 'Boston' in mytuple:
    print('yes')
else:
    print('no')

if 'Tim' in mytuple:
    print('yes')
else:
    print('no')

my_tuple = ('a', 'p', 'p', 'l', 'e')

print(len(my_tuple))
print(my_tuple.count('p'))
print(my_tuple.index('p'))
print(my_tuple.index('e'))

my_list = list(my_tuple)
print(my_list) # Returns as list enclosed in [] brackets

my_tuple2 = tuple(my_list)
print(my_tuple2) # Returns as tuples enclosed in () parenthesis

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = a[2:5]
print(b)

print(a[2:])
print(a[::1])
print(a[::2])
print(a[::-1])

my_tuple3 = 'Max', 28, 'Boston'

name, age, city = my_tuple3 # Unpacking
print(name)
print(age)
print(city)

my_tuple4 = (0, 1, 2, 3, 4)

i1, *i2, i3 = my_tuple4
print(i1) # 0, first item
print(i3) # 4, second item
print(*i2) # 1 2 3, middle items using *
print(i2) # [1, 2, 3], converted into list

import sys

my_list = [0, 1, 2, 'hello', True]
my_tuple = (0, 1, 2, 'hello', True)
print(sys.getsizeof(my_list), 'bytes') # 104 bytes
print(sys.getsizeof(my_tuple), 'bytes') # 80 bytes

import timeit
print(timeit.timeit(stmt='[0, 1, 2, 3, 4, 5]', number=1000000))
# 0.14s, 0.14471610001055524
print(timeit.timeit(stmt='(0, 1, 2, 3, 4, 5)', number=1000000))
# 0.02s, 0.025830899947322905