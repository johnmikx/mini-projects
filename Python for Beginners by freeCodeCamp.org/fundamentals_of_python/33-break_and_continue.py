items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue  # Skip the rest of the loop when item is 2
    print(item)  # This will print 1, 3, 4

items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        break # Exit the loop when item is 2
    print(item) # This will print 1 and then exit the loop