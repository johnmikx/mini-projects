"""
Objectives: 

- We will talk about copying
- We will learn how we can copy mutable element with a built-in copy module
- The difference between shallow and deep copies
- We will also have a look at how to make actual copies of custom objects
"""

org = 5
cpy = org
cpy = 6
print(cpy) # 6
print(org) # 5

org = [0, 1, 2, 3 ,4]
cpy = org
cpy[0] = -10
print(cpy) # [-10, 1, 2, 3, 4]
print(org) # [-10, 1, 2, 3, 4]

import copy
org = [0, 1, 2, 3 ,4]
cpy = copy.copy(org) # <-- shallow copy
cpy[0] = -10
print(cpy) # [-10, 1, 2, 3, 4]
print(org) # [0, 1, 2, 3, 4]

org = [0, 1, 2, 3 ,4]
cpy = org.copy() # <-- shallow copy (list method)
cpy[0] = -10
print(cpy) # [-10, 1, 2, 3, 4]
print(org) # [0, 1, 2, 3, 4]

org = [0, 1, 2, 3 ,4]
cpy = list(org) # <-- shallow copy
cpy[0] = -10
print(cpy) # [-10, 1, 2, 3, 4]
print(org) # [0, 1, 2, 3, 4]

org = [0, 1, 2, 3 ,4]
cpy = org[:] # <-- shallow copy via slicing
cpy[0] = -10
print(cpy) # [-10, 1, 2, 3, 4]
print(org) # [0, 1, 2, 3, 4]

org = [[0, 1, 2, 3 ,4], [5, 6, 7, 8, 9]] # 2D list (a list containing two inner lists)
cpy = org[:]
cpy[0][1] = -10 # Modifying the second element (index 1) of the first inner list
print(cpy) # [[0, -10, 2, 3, 4], [5, 6, 7, 8, 9]]
print(org) # [[0, -10, 2, 3, 4], [5, 6, 7, 8, 9]]

org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org) # Deep copy of org (copies inner lists too)
cpy[0][1] = -10 # Modify cpy only

# Print both to show org is unaffected
print(cpy)  # [[0, -10, 2, 3, 4], [5, 6, 7, 8, 9]]  <-- deep copy
print(org)  # [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]  <-- shallow copy

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age =age

p1 = Person('Alex', 27)
p2 = p1

p2.age = 28
print(p2.age) # 28
print(p1.age) # 28

p1 = Person('Alex', 27)
p2 = copy.copy(p1) # <-- shallow copy

p2.age = 28
print(p2.age) # 28
print(p1.age) # 27 <-- shallow copy

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age =age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Alex', 55)
p2 = Person('Joe', 27)

company = Company(p1, p2)
company_clone = copy.copy(company)
company_clone.boss.age = 56
print(company_clone.boss.age) # 56
print(company.boss.age) # 56

p1 = Person('Alex', 55)
p2 = Person('Joe', 27)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age) # 56
print(company.boss.age) # 55