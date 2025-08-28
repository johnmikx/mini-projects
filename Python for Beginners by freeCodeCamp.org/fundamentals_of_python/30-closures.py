def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

increment = counter()

print(increment()) # Output: 1
print(increment()) # Output: 2
print(increment()) # Output: 3
print(increment()) # Output: 4
print(increment()) # Output: 5