# Identity operator: is
a = [1, 2, 3] # Identity A
b = a
c = [1, 2, 3] # Identity B, different object with same contents

print("a is b:", a is b)   # True, because b references the same object as a
print("a is c:", a is c)   # False, because c is a different object with the same contents

# Membership operator: in
numbers = [1, 2, 3, 4, 5]
print("3 in numbers:", 3 in numbers)     # True, 3 is in the list
print("6 in numbers:", 6 in numbers)     # False, 6 is not in the list

text = "hello"
print("'e' in text:", 'e' in text)       # True, 'e' is in the string
print("'a' in text:", 'a' in text)       # False, 'a' is not