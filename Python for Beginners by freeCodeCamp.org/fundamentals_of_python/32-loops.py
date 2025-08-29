condition = True

while condition == True: # This loop will run indefinitely because the condition is always True
    print("The condition is True") # This line will be printed repeatedly
    condition = False # Change the condition to False to stop the loop

count = 0
while count < 10:
    print("The condition is True")
    count += 1 # Increment count by 1, count = count + 1

print("The loop has ended")

items = [1, 2, 3, 4, 5]
for item in items:
    print(item) # This will print each item in the list

for item in range(15):
    print(item) # This will print numbers from 0 to 14

items = [1, 2, 3, 4, 5]
for index, item in enumerate(items):
    print(index, item) # This will print the index and the item at that index

items = ["beua", "syd", "quincy"]
for index, item in enumerate(items):
    print(index, item)    