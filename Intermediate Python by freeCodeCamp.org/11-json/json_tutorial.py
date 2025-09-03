# JSON is short for JavaScript Object Notation. And it's a lightweight data format
# that is used for data exchange. It's heavily used in web applications, so you
# should be comfortable working with it. Luckily, Python already comes with a built-in
# JS module that makes working with JSON data very easy. We will have a look at how
# we can encode and decode JSON data with this module.

# Let's say we have a Python dictionary and we want to convert it to a JSON format.
# And this is also called "serialization" or "encoding".

# From Python dictionary to a JSON object:
import json

person = {"name": "John",
          "age": 30,
          "city": "New York",
          "hasChildren": False,
          "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person)
print(personJSON)
# Output: {"name": "John", "age": 30, "city": "New York", "hasChildren": false, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4) # Optional Parameters: separators= and sort_keys=
print(personJSON)
# Output:
# {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "hasChildren": false,
#     "titles": [
#         "engineer",
#         "programmer"
#     ]
# }

# Note: dumps = dump + s (which 's' stands for string)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

# Let's say we have JSON data and we want to convert it back to Python object.
# And this is also called "deserialization" or "decoding".

person = json.loads(personJSON)
print(person) # {'name': 'John', 'age': 30, 'city': 'New York', 'hasChildren': False, 'titles': ['engineer', 'programmer']}

# Note: loads = load + s (which 's' stands for string)

with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name,
                'age': o.age,
                o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(user, default=encode_user)
print(userJSON) # {"name": "Max", "age": 27, "User": true}

from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name,
                    'age': o.age,
                    o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
    
userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON) # {"name": "Max", "age": 27, "User": true}

userJSON = UserEncoder().encode(user)
print(userJSON) # {"name": "Max", "age": 27, "User": true}

user = json.loads(userJSON)
print(user) # {'name': 'Max', 'age': 27, 'User': True}

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'],
                    age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(user.name) # Max