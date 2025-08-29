class Animal:
    def walk(self):
        print("Walking...")

class Dog(Animal): # Inheritance
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def bark(self):
        print("woof!")

roger = Dog("Roger", 9)
print(type(roger)) # <class '__main__.Dog'>

print(roger.name) # Roger
print(roger.age) # 9

roger.bark() # woof!
roger.walk() # Walking...