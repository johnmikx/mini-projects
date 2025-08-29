# MAP
numbers = [1, 2, 3]

def double(a):
    return a * 2 # Lambda version below

result = map(double, numbers)

print(result) # <map object at 0x0000024E4CB815A0>
print(list(result)) # [2, 4, 6]

numbers2 = [4, 5, 6]

double = lambda a : a * 2

result2 = map(double, numbers2)

print(result2) # <map object at 0x0000024400E41930>
print(list(result2)) # [8, 10, 12]

# More Simplified, substitute lambda function inside double

numbers2 = [4, 5, 6]

result2 = map(lambda a : a * 2, numbers2)

print(result2)
print(list(result2))

# FILTER
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda n : n % 2 == 0, numbers)

print(list(result))

# REDUCE
expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]

sum = 0

for expense in expenses:
    sum += expense[1] # sum = sum + expense[1]

print(sum)

# Quicker way of REDUCE
from functools import reduce

expenses = [
    ('Dinner', 80), # a[0] is 'Dinner' and a[1] is 80
    ('Car repair', 120) # b[0] is 'Car repair' and b[1] is 120
]

sum = reduce(lambda a, b: a[1] + b[1], expenses)

print(sum)