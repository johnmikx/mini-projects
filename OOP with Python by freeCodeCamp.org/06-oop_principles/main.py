from item import Item
from keyboard import Keyboard

item1 = Keyboard("jscPhone", 1000, 3)

item1.apply_discount()

print(item1.price)