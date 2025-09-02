# Dictionary: key-value pairs, unordered, mutable
# Description: A dictionary is a collection data type that is unordered 
# and mutable. It consists of a collection of key-value pairs. So each
# key-value pairs maps the key to its associated value.

mydict = {}

mydict = {'name': 'Max', 'age': 28, 'city': 'New York'}
print(mydict)

mydict2 = dict(name='Mary', age=27, city='Boston')
print(mydict2)

value = mydict['name']
print(value)

print(mydict['age'])
print(mydict['city'])
# print(mydict['lastname']) # KeyError: 'lastname'

mydict['email'] = 'max@xyz.com'
print(mydict)

mydict['email'] = 'coolmax@xyz.com'
print(mydict)

del mydict['name'] # Option 1 for Deletion
print(mydict)

mydict.pop('age') # Option 2 for Deletion
print(mydict)

mydict.popitem() # Removes the last key-value pair
print(mydict)

mydict2 = {'name': 'Max', 'age': 28, 'city': 'New York'}

if 'name' in mydict2:
    print(mydict2['name'])

try:
    print(mydict2['name'])
except:
    print('Error')

try:
    print(mydict2['lastname'])
except:
    print('Error')

for key in mydict2: # Option 1: key
    print(key)

for key in mydict2.keys(): # Option 2: key, same thing as Option 1
    print(key)

for value in mydict2.values(): # value
    print(value)

for key, value in mydict2.items(): # For both key-value pairs
    print(key, value)

mydict2_cpy = mydict2

mydict2_cpy['email'] = 'max@xyz.com'
print(mydict2_cpy) # Same Output
print(mydict2) # Same Output

# mydict2_cpy = mydict2.copy() # Option 1
# mydict2_cpy = dict(mydict2) # Option 2

# mydict2_cpy['email'] = 'max@xyz.com'
# print(mydict2_cpy) # Output: {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@xyz.com'}
# print(mydict2) # Output: {'name': 'Max', 'age': 28, 'city': 'New York'}

my_dict = {'name': 'Max', 'age': 28, 'email': 'max@xyz.com'}
my_dict_2 = dict(name='Mary', age=27, city='Boston')

my_dict.update(my_dict_2) # Key-value pairs got overwritten
print(my_dict)

my_dict_3 = {3: 9, 6: 36, 9: 81}
print(my_dict_3)

# value = my_dict_3[0] # KeyError: 0, Must access it's ACTUAL KEY
value = my_dict_3[3] 
print(value) # 9

mytuple = (8, 7)
mydict3 = {mytuple: 15}
print(mydict3) # {(8, 7): 15}

# mytuple = [8, 7]
# mydict3 = {mytuple: 15}
# print(mydict3) # TypeError: unhashable type: 'list'
# That's because a list is mutable and can be changed after its creation.
# And therefore it's also not hashable and cannot be used as a key.
# So be careful here!