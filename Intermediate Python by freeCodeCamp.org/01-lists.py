# Lists: ordered, mutable, allows duplicate elements
# Description: A list is a collection data type that is ordered, mutable,
# and that allows duplicate elements.

mylist0 = []

mylist = ['banana', 'cherry', 'apple']
print(mylist)

mylist2 = list()
print(mylist2)

mylist3 = [5, True, 'apple', 'apple']
print(mylist3)

for i in mylist:
    print(i)

if 'banana' in mylist:
    print('yes')
else:
    print('no')

print(len(mylist))

mylist.append('lemon')
print(mylist)

mylist.insert(1, 'blueberry')
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

item2 = mylist.remove('cherry')
print(mylist)

item = mylist[-2]
print(item)

# item = mylist.clear() # removes all the items in the list

item = mylist.reverse()
print(mylist)

mylist4 = [4, 3, 1, -1, -5, 10]
print(mylist4)

# item = mylist4.sort()

new_list = sorted(mylist4)
print(mylist4)
print(new_list)

mylist5 = [0] * 5
print(mylist5)

mylist6 = [1, 2, 3, 4, 5]
new_list2 = mylist5 + mylist6
print(new_list2)

mylist7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(mylist7[1:5])
print(mylist7[::1]) # [start:stop:skip]
print(mylist7[::2])
print(mylist7[::-1])

list_org = ['banana', 'cherry', 'apple']

list_cpy = list_org.copy() # Option 1: put .copy() function to keep the actual list
list_cpy = list(list_org) # Option 2
list_cpy = list_org[:] # Option 3

list_cpy.append('lemon')
print(list_cpy)
print(list_org)

# List Comprehension
mylist8 = [1, 2, 3, 4 , 5, 6]
b = [i*i for i in mylist8] # Squared as i*i or i^2

print(mylist)
print(b)