age = 8 # Global variable

def test():
    print(age) # Accessing the global variable 'age' inside the function

print(age) # Output: 8
test() # Output: 8


def test():
    age2 = 10 # Local variable
    print(age2) # Accessing the local variable 'age' inside the function

    print(age2) # Output: 10
    test() # Output: 10