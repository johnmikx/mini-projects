"""
__init__ method is a method with a unique name that you need to call it the
way it is intentionally, in order to its special features.

The collection of those __name__ methods are used to be called magic methods.
"""

class Item:
    def __init__(self, name):
        print(f"An instance created: {name}")

    def calculate_total_price(self, x, y):
        return x * y

item1 = Item("Phone")
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

item2 = Item("Laptop")
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3

# Output:
"""
An instance created: Phone
An instance created: Laptop
"""

class Item:
    def __init__(self, name):
        self.name = name

    def calculate_total_price(self, x, y):
        return x * y

item1 = Item("Phone")
item1.price = 100
item1.quantity = 5

item2 = Item("Laptop")
item2.price = 1000
item2.quantity = 3

print(item1.name)
print(item2.name)

# Output:
"""
Phone
Laptop
"""

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return x * y

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)

# Output:
"""
Phone
Laptop
100
1000
5
3
"""

class Item:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return x * y

item1 = Item("Phone", 100)
item2 = Item("Laptop", 1000)

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)

# Output:
"""
Phone
Laptop
100
1000
0
0
"""

class Item:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

# Output:
"""
100
3000
"""