import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount | they'll pay the 80%
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater than zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    def __repr__(self): # represent magic method
        return f"Item('{self.name}', {self.price}, {self.quantity})"

Item.instantiate_from_csv()
print(Item.all)

# Output:
"""
[Item('Phone', 100.0, 1),
Item('Laptop', 1000.0, 3),
Item('Cable', 10.0, 5),
Item('Mouse', 50.0, 5),
Item('Keyboard', 75.0, 5)]
"""