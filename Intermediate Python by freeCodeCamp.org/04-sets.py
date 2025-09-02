# Sets: unordered, mutable, no duplicates
# Description: A set is a collection data type. Unlike lists, or tuples,
# it does not allow duplicate elements. A set is created with braces,
# just like a dictionary, but we don't put key value pairs in it.
# Instead just single elements separated by comma.

myset = {}

myset = {1, 2, 3}
print(myset) # {1, 2, 3}

myset = {1, 2, 3, 1, 2}
print(myset) # {1, 2, 3}, a set does not allow duplicates

myset = set([1, 2, 3])
print(myset) # {1, 2, 3}

myset = set('Hello')
print(myset) # {'o', 'e', 'l', 'H'} | Note: The order is arbitrary
# Because a set is unordered, and the order is not important

myset = {}
print(type(myset)) # <class 'dict'> | Recognized as dictionary

myset = set()
print(type(myset)) # <class 'set'>

myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

# myset.remove(3) # Option 1 for removing an element
# myset.discard(2) # Option 2 for removing an element
# myset.clear() # set(), removes all the elements
# print(myset.pop()) # 1 
# print(myset)

for i in myset:
    print(i)

if 1 in myset:
    print('yes')

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens) # odds union evens
print(u) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

i = odds.intersection(evens) # odds intersection evens
print(i) # set(), empty set

i = odds.intersection(primes) # odds intersection primes
print(i) # {3, 5, 7}

i = evens.intersection(primes) # evens intersection primes
print(i) # {2}

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB) # setA - setB
print(diff) # {4, 5, 6, 7, 8, 9}

diff = setB.difference(setA) # setB - setA
print(diff) # {10, 11, 12}

diff = setB.symmetric_difference(setA) # (setA - setB) union (setB - setA)
print(diff) # {4, 5, 6, 7, 8, 9, 10, 11, 12}

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.update(setB) # It's `union` update of both sets A and B
print(setA) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.intersection_update(setB) # It's `intersection` update of both sets A and B
print(setA) # {1, 2, 3}

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.difference_update(setB) # setA - setB
print(setA) # {4, 5, 6, 7, 8, 9}

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.symmetric_difference_update(setB) # (setA - setB) union (setB - setA)
print(setA) # {4, 5, 6, 7, 8, 9, 10, 11, 12}

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}

# Subsets
# Contains only elements that are part of the superset; 
# it is a smaller or equal-sized set. 
print(setA.issubset(setB)) # False
print(setB.issubset(setA)) # True

# Supersets
# Contains all the elements of the subset, and possibly more; 
# it is a larger or equal-sized set. 
print(setA.issuperset(setB)) # True
print(setB.issuperset(setA)) # False

# Disjoint Sets
# Two sets are disjoint if they have no elements in common.
print(setA.isdisjoint(setB)) # False
print(setA.isdisjoint(setC)) # True


# For copies
setA = {1, 2, 3, 4, 5, 6}
setB = setA
setB.add(7)

print(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = setA.copy()
setB.add(7)

print(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = set(setA)
setB.add(7)

print(setB)
print(setA)

# Frozen Set
a = frozenset([1, 2, 3, 4])

# a.add(2) # AttributeError: 'frozenset' object has no attribute 'add'
# a.remove(1) # AttributeError: 'frozenset' object has no attribute 'remove'

print(a) # frozenset({1, 2, 3, 4})