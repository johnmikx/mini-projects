def hello():
    print("Hello, World!")

hello() # Arguments can have default value that is used if no argument is passed
hello()
hello()

def hello(name): # Note: Parameters are "variables" that hold the values you pass to a function
    print("Hello! " + name)

hello("Bow") # Note: Arguments are the "values" you pass to a function when you call it
# hello() # This will raise an error because the function expects an argument
# TypeError: hello() missing 1 required positional argument: 'name'

def hello(name="my friend"): # Default parameter value
    print("Hello! " + name)

hello() # Now this works, using the default value
hello("Bow") # You can still pass an argument to override the default value

def hello(name, age):
    print("Hello! " + name + ", you are " + str(age) + " years old.")

hello("Mike", 30) # Correct usage

def change(value):
    value["name"] = "Syd"

val = {"name": "Zoe"}
change(val)

print(val) # Output: {'name': 'Syd'}

def hello(name):
    if not name:
        return
    print("Hello! " + name) # Function will exit if name is empty or None


hello(False) # No output, function exits early
hello("Mike") # Output: Hello! Mike

def hello(name):
    print("Hello! " + name + "!")
    return name, "Baki", 8

print(hello("Bow")) # Output: ('Bow', 'Baki', 8)