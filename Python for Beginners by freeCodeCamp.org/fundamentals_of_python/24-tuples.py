names = ("Xander", "Yvonne", "Zach")

print(names[0])  # Output: Xander
print(names.index("Yvonne"))  # Output: 1
print(len(names))  # Output: 3

print("Zach" in names)  # Output: True
print(names[0:2])  # Output: ('Xander', 'Yvonne')
print(sorted(names))  # Output: ['Xander', 'Yvonne', 'Zach']

newTuple = names + ("Alice", "Bob")