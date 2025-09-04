class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater than zero!'

        # Assign to self object
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

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount | they'll pay the 80%
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater than zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

# Output:
"""
0.8
0.8
0.8
"""

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount | they'll pay the 80%
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater than zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

print(Item.__dict__)  # All the attributes for Class level
print(item1.__dict__) # All the attributes for instance level

# Output:
"""
{'__module__': '__main__', 'pay_rate': 0.8, '__init__': <function Item.__init__ at 0x000001BE1375BB00>,
'calculate_total_price': <function Item.calculate_total_price at 0x000001BE1375BBA0>,
'__dict__': <attribute '__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None}
{'name': 'Phone', 'price': 100, 'quantity': 1}
"""