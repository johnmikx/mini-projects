dog = {
    'name': 'Roger',
    'age': 8,
    'color': 'green'
}
# Note: Key-value pairs, unordered, keys must be unique and immutable (strings, numbers, tuples)

dog['name'] = 'Sydney'  # Modifying value by key
print(dog['name'])  # Accessing value by key
print('color' in dog)  # Check if key exists
print(dog.keys())  # dict_keys(['name', 'age', 'color'])
print(dog.values())  # dict_values(['Sydney', 8, 'green'])
print(dog.items())  # dict_items([('name', 'Sydney'), ('age', 8), ('color', 'green')])

dog2 = {
    'name': 'Michael',
    'age': 9,
    'color': 'brown'
}

dog2['food'] = 'meat' # Adding new key-value pair
print(dog2)

del dog2['color'] # Deleting key-value pair

print(dog2.get('color', 'brown'))
print(dog2.pop('name')) # Removes key and returns its value
print(dog2.popitem()) # Removes and returns an arbitrary key-value pair
print(len(dog2)) # Length of dictionary

dogCopy = dog2.copy() # Shallow copy of dictionary
print(dogCopy)