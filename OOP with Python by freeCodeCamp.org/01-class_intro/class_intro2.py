# Creating our first class:
"""
It is divided into two parts,

- The first one will be the creation of the class.
- The second one will be the part that I will instantiate some objects of
this class.

Creating an instance or creating an object is the same thing.
"""

class Item:
    pass

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(type(item1))          # <class '__main__.Item'>
print(type(item1.name))     # <class 'str'>
print(type(item1.price))    # <class 'int'>
print(type(item1.quantity)) # <class 'int'>

random_str = "aaa"
print(random_str.upper())