items = ["Rex", "Fido", 1, "Ginger", True, "Quincy", 7]

# items.sort() # sorts the list in place 
# print(items) # TypeError: '<' not supported between instances of 'int' and 'str'

items2 = ["rex",  "Rex", "Fido", "Ginger", "Quincy"]

itemscopy = items2[:] # makes a copy of the list
items2.sort(key=str.lower) # sorts the list in place, ignoring case

print(items2)
print(itemscopy)
print(sorted(itemscopy, key=str.lower)) # returns a new sorted list, ignoring case