condition1 = True
condition2 = False

not condition1 # False, "Not"
condition1 and condition2 # False, "And"
condition1 or condition2 # True, "Or"

# Note: True and False are boolean values in Python
# They can also be represented as 1 (True) and 0 (False) in numerical contexts.

print(0 or 1) # Outputs: 1
print(False or 'hey') # Outputs: 'hey'
print('hi' or 'hey') # Outputs: 'hi'
print([] or False) # Outputs: 'False'
print(False or []) # Outputs: '[]'

print(0 and 1) # Outputs: 0
print(1 and 0) # Outputs: 0
print(False and 'hey') # Outputs: False
print('hi' and 'hey') # Outputs: 'hey'
print([] and False) # Outputs: []
print(False and []) # Outputs: False