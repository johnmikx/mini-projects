# lambda arguments: expression
# Description: lambda function is a small one line anonymous function that
# is defined without a name. First it has a lambda keyword, then it can
# take some arguments, then a colon, and then an expression. This will create
# a function with some arguments, and it evaluates the expression and returns
# the results.

# lambda arguments: expression
add10 = lambda x: x + 10
print(add10(5)) # 15

# This is practically same as normal function like this:
def add10_func(x):
    return x + 10

print(add10_func(5)) # 15

mult = lambda x, y: x*y
print(mult(2, 7)) # 14

# lambda functions are typically used when you need a simple function that
# is used only once in your code. Or it is used as an argument to higher
# order functions, meaning functions that take in other functions as arguments.

# For example, they are used along with the built-in functions like sorted(),
# map(), filter(), and reduce(), and we will have a look at all of them to make
# the usage of lambda.

# By default, this will sort our list by the first argument (x argument).
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
print(points2D) # [(1, 2), (15, 1), (5, -1), (10, 4)]
print(points2D_sorted) # [(1, 2), (5, -1), (10, 4), (15, 1)]


# This sorts the second argument (y argument) by key=lambda x: x[1]
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D) # [(1, 2), (15, 1), (5, -1), (10, 4)]
print(points2D_sorted) # [(5, -1), (15, 1), (1, 2), (10, 4)]

def sort_by_y(x): # This will return the same result
    return x[1]

points2D_sorted = sorted(points2D, key=sort_by_y)
print(points2D) # [(1, 2), (15, 1), (5, -1), (10, 4)]
print(points2D_sorted) # [(5, -1), (15, 1), (1, 2), (10, 4)]

# This sorts according to their sums of each tuple
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D_sorted) # [(1, 2), (5, -1), (10, 4), (15, 1)]

# The map() function transforms each element with a function.
# map(func, seq)

a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(b) # <map object at 0x00000205938220E0>
print(list(b)) # [2, 4, 6, 8, 10]

# This is preferred one using list comprehension
c = [x*2 for x in a]
print(c) # [2, 4, 6, 8, 10]

# The filter() function also gets a function and a sequence. This function
# must return True or False. And the filter() function will return all elements
# for which the function evaluates to True.
# filter(func, seq)

a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2==0, a)
print(list(b)) # [2, 4, 6] | Even numbers as x % 2 == 0

# This is preferred one using list comprehension
c = [x for x in a if x%2==0]
print(c) # [2, 4, 6]

from functools import reduce
# The reduce() function repeatedly applies the function to the elements
# and returns a single value.
# reduce(func, seq)

a = [1, 2, 3, 4, 5, 6]

product_a = reduce(lambda x,y: x*y, a)
print(product_a) # 1 * 2 * 3 * 4 * 5 * 6 = 720