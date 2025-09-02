# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
# Description: The itertoos module is a collection of tools for handling
# iterators. Simply put iterators are data types that can be used in a
# for loop. So for example, the most common iterator is the list.

from itertools import product
a = [1, 2]
b = [3, 4]

prod = product(a, b)
print(prod) # <itertools.product object at 0x0000026D28F28D00>
print(list(prod)) # [(1, 3), (1, 4), (2, 3), (2, 4)]

a = [1, 2]
b = [3]

prod = product(a, b, repeat=2)
print(list(prod)) # [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

from itertools import permutations
a = [1, 2, 3]

perm = permutations(a)
print(list(perm)) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

perm = permutations(a, 2)
print(list(perm)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]

comb = combinations(a, 2)
print(list(comb)) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr)) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

from itertools import accumulate
# The accumulate function makes an iterator that returns accumulated sums
# or any other binary function that I will give as input.
a = [1, 2, 3, 4]

acc = accumulate(a)
print(list(acc)) # [1, 3, 6, 10]
# 1 = 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10

import operator
acc = accumulate(a, func=operator.mul)
print(list(acc)) # [1, 2, 6, 24]
# 1 = 1
# 1 * 2 = 2
# 1 * 2 * 3 = 6
# 1 * 2 * 3 * 4 = 24

a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(list(acc)) # [1, 2, 5, 5, 5]

from itertools import groupby
# The groupby function makes an iterator that returns keys and groups from
# an iterable.

def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]

group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))
    # True [1, 2], x < 3
    # False [3, 4], x is not < 3

group_obj = groupby(a, key=lambda x: x<3)
# lambdas are small one line function that can have an input and will do
# some expression and then will return an output.
for key, value in group_obj:
    print(key, list(value))
    # True [1, 2], x < 3
    # False [3, 4], x is not < 3

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

group_obj = groupby(persons, key=lambda x: x['age']) # group by same 'age'
for key, value in group_obj:
    print(key, list(value))
    # 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
    # 27 [{'name': 'Lisa', 'age': 27}]
    # 28 [{'name': 'Claire', 'age': 28}]

# Infinite Iterators
from itertools import count, cycle, repeat

a = [1, 2, 3]
for i in count(10):
    print(i) # This is infinite count to infinity
    if i == 15:
        break

a = [1, 2, 3]
# for i in cycle(10):
#    print(i) # This is infinite cycle of 1, 2, 3

# for i in repeat(1):
#    print(i) # This is infinite repeat of 1's

for i in repeat(1, 4):
    print(i) # This only repeats four times