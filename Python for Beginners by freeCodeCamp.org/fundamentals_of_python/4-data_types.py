name = 'Sinusoid'
print(name)  # Sinusoid
print(type(name))  # <class 'str'>
print(type(name) == str)  # True
print(isinstance(name, str))  # True

age = 25
print(isinstance(age, int)) # True
print(isinstance(age, float)) # False
print(isinstance(age, (int, float))) # True

height = 5.9
print(isinstance(height, float)) # True
print(isinstance(height, int)) # False

weight = '20'
print(type(weight))  # <class 'str'>

# Class Constructors
artificial_float = float(age) # Casting int to float
print(artificial_float)  # 25.0
print(type(artificial_float))  # <class 'float'>
print(isinstance(artificial_float, float))  # True

artificial_weight = int(weight) # Casting str to int
print(type(weight))  # <class 'int'>

# Other data types
complex # for complex numbers
bool # for boolean values (True or False)
list # for ordered collection of items (mutable)
tuple # for ordered collection of items (immutable)
range # for a sequence of numbers
dict # for key-value pairs (dictionary)
set # for unordered collection of unique items
frozenset # for immutable sets
bytes # for binary data (immutable)
bytearray # for binary data (mutable)
memoryview # for memory views of binary data