# Generators or functions that return an object that can be iterated over.
# And the special thing is that they generate the items inside the object
# lazily, which means they generate the items only one at a time and only
# when you ask for it. And because of this, they are much more memory efficient
# than other sequence objects when you have to deal with large data sets.
# They are powerful advanced Python technique.

# A generator is defined like a normal function, but with the yield keyword
# instead of the return keyword.

def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
print(g) # <generator object mygenerator at 0x0000018174A54CA0>

# for i in g:
#     print(i)

value = next(g)
print(value) # 1

value = next(g)
print(value) # 2

value = next(g)
print(value) # 3


def mygenerator():
    yield 3
    yield 2
    yield 1

g = mygenerator()

# print(sum(g)) # 6

print(sorted(g)) # [1, 2, 3]

def countdown(num):
    print('Starting') #  Starting
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

value = next(cd)
print(value) # 4

print(next(cd)) # 3
print(next(cd)) # 2
print(next(cd)) # 1

import sys

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(firstn(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(firstn(10))) # 45

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn(10))) # 45
print(sum(firstn_generator(10))) # 45

print(sys.getsizeof(firstn(100000))) # 800984
print(sys.getsizeof(firstn_generator(100000))) # 192

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)

mygenerator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator)) # 200


mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist)) # 4216