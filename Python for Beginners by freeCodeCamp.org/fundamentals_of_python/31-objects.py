age = 8 # integer

print(age.real) # 8
print(age.imag) # 0
print(age.bit_length()) # 4

items = [1, 2]

items.append(3) # adds 3 to the end of the list
print(items) # [1, 2, 3]

items.pop() # removes the last item from the list
print(items) # [1, 2]

print(id(items)) # e.g. 140353303208960

age = 8

age += 1 # age = age + 1