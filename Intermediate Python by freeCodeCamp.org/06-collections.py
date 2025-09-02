# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
# Description: The collections module implements special container data
# types, and provides alternatives with some additional functionality
# compared to the general BERT (Bidirectional Encoder Representations 
# from Transformers) and containers, like dictionaries, lists or tuples. 
# So we will be talking about five different types from the collections
# module, the Counter, the namedtuple, the OrderedDict, defaultdict, deque

from collections import Counter
# The Counter is a container that stores the elements as dictionary keys
# and their counts as dictionary values.

a = 'aaaaabbbbccc'
my_counter = Counter(a)
print(my_counter) # Counter({'a': 5, 'b': 4, 'c': 3})

a = 'aaaaabbbbccc'
my_counter = Counter(a)
print(my_counter.items()) # dict_items([('a', 5), ('b', 4), ('c', 3)])

a = 'aaaaabbbbccc'
my_counter = Counter(a)
print(my_counter.keys()) # dict_keys(['a', 'b', 'c'])

a = 'aaaaabbbbccc'
my_counter = Counter(a)
print(my_counter.values()) # dict_values([5, 4, 3])

a = 'aaaaabbbbccc'
my_counter = Counter(a)
print(my_counter) # Counter({'a': 5, 'b': 4, 'c': 3})
print(my_counter.most_common(1)) # [('a', 5)]
print(my_counter.most_common(2)) # [('a', 5), ('b', 4)]
print(my_counter.most_common(1)[0]) # ('a', 5)
print(my_counter.most_common(1)[0][0]) # a

print(my_counter.elements()) # <itertools.chain object at 0x000002206884DB10>
# must convert it into lists

print(list(my_counter.elements())) # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']

from collections import namedtuple
# The namedtuple is an easy to create and lightweight object type, similar
# to a struct (a module provides functionality for converting between Python 
# values and C-style binary data, represented as Python bytes objects.)

Point = namedtuple('Point', 'x, y')
# Class called 'Point'
# Fields called 'x' and 'y'

pt = Point(1, -4)
print(pt) # Point(x=1, y=-4)
print(pt.x, pt.y) # 1 -4

from collections import OrderedDict
# The OrderedDict is just like a regular dictionary, but they remember the
# order that the items were inserted. They have become less important now
# since the built in dictionary class has also the ability to remember the
# order since Python 3.7. This is guaranteed.

# For example, if you use an older Python version, this may be a way to use
# a dictionary that remembers the order.

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict) # OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
print(ordered_dict) # OrderedDict({'b': 2, 'c': 3, 'd': 4, 'a': 1})

ordered_dict = {}
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}, Newer Version

from collections import defaultdict
# The defaultdict is also similar to the usual dictionary container, with
# the only difference that it will have a default value of the key that
# has not been set yet.

d = defaultdict(int)
d['a'] = 1
d['b'] = 2

print(d) # defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(d['a']) # 1
print(d['b']) # 2
print(d['c']) # 0, since it is does not exist in dictionary


d = defaultdict(float)
d['a'] = 1
d['b'] = 2

print(d['c']) # 0.0, since it is does not exist in dictionary

d = defaultdict(list)
d['a'] = 1
d['b'] = 2

print(d['c']) # [], since it is does not exist in dictionary

d = {}
d['a'] = 1
d['b'] = 2

# print(d['c']) # KeyError: 'c'

from collections import deque
# The deque (pronounced as deck) is a double-ended queue. It can be used
# to add or remove elemets from both ends. And both are implemented in a
# way that this will be very efficiently.

d = deque()
d.append(1)
d.append(2)

print(d) # deque([1, 2])

d.appendleft(3)
print(d) # deque([3, 1, 2])

d.pop()
print(d) # deque([3, 1]), removes the right element

d.popleft()
print(d) # deque([1]), removes the left element

d.clear()
print(d) # deque([]), removes all the elements

d.append(1)
d.append(2)
d.append(3)
d.extend([4, 5, 6])
print(d) # deque([1, 2, 3, 4, 5, 6])

d.extendleft([4, 5, 6])
print(d) # deque([6, 5, 4, 1, 2, 3, 4, 5, 6])

d.rotate(1)
print(d) # deque([6, 6, 5, 4, 1, 2, 3, 4, 5])

d.rotate(2)
print(d) # deque([4, 5, 6, 6, 5, 4, 1, 2, 3])

d.rotate(-1)
print(d) # deque([5, 6, 6, 5, 4, 1, 2, 3, 4])

d.rotate(-2)
print(d) # deque([6, 5, 4, 1, 2, 3, 4, 5, 6])