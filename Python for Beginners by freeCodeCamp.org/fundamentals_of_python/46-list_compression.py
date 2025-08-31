# Method 1:
numbers = [1, 2, 3, 4, 5]

numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)

# Method 2:
numbers_power_2 = []

for n in numbers:
    numbers_power_2.append(n**2)

print(numbers_power_2)

# Method 3:
numbers_power_2 = list(map(lambda n : n**2, numbers))

print(numbers_power_2)