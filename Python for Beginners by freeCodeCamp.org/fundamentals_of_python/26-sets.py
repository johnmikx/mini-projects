set1 = {"Xander", "Yvonne", "Zach"}
set2 = {"Alice", "Bob", "Charlie", "Xander"}

intersection = set1 & set2
print(intersection)  # Output: {'Xander'}

union = set1 | set2
print(union)  # Output: {'Alice', 'Bob', 'Charlie', 'Xander', 'Yvonne', 'Zach'}

difference = set1 - set2 # items in set1 but not in set2
print(difference)  # Output: {'Yvonne', 'Zach'}

difference = set2 - set1 # items in set2 but not in set1
print(difference)  # Output: {'Alice', 'Bob', 'Charlie'}

print(list(set1))  # Convert set to list