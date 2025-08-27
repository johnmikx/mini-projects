name = 'Zortex'

print(name[0])  # First character
print(name[1])  # Second character
print(name[-1]) # Last character
print(name[-2]) # Second last character
print(name[1:4]) # Characters from index 1 (inclusive) to 4 (exclusive) | [1, 4)
print(name[1:])  # Characters from index 1 to end | [1, 0)
print(name[:4])  # Characters from start to index 4 (exclusive) | [0, 4)
print(name[:3])  # First three characters, 3 is exclusive | [0, 3)