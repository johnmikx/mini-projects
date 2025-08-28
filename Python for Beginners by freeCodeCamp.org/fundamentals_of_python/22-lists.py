dogs = ["Rex", "Fido", 1, "Ginger", True, "Quincy", 7]

print("Rex" in dogs)
print("Beau" in dogs)
print(dogs[0])

dogs[2] = "Spot"
dogs.append("Moises")
dogs.extend(["Beau", "Lassie", 5])
dogs += ["Loki", "Max"]
dogs.remove("Fido")
print(dogs)

print(dogs[-2])
print(dogs[2:4]) # slicing, [2, 4)
print(dogs[1:])  # from index 1 to the end 
print(dogs[:3])  # from the start to index 3 (not including 3)
print(len(dogs))

print(dogs.pop()) # removes and returns the last item

items = ["Rex", "Fido", 1, "Ginger", True, "Quincy", 7]

items.insert(2, "Test") # insert at index 2
items[1:1] = ["Test2", "Test3"] # insert at index 1
print(items)