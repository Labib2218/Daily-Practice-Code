list1 = ['labib', 'habib', 'tabib', 'sabib', 'sakib', 'akib', 'rakib']
print(list1)
list2 = [1, 2, 152, 78, 68, 55, 7, 5, 8, 9, 58, 65]
print(list2)

# Change list item by index number
list1[3] = 'noman'
print(list1)
print(list1[2])

# access list item
for i in list2:
    print(i * 3)

# list comprehension
n = [i * 5 for i in list2]
print(n)

# sorting list
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)

# Add 2 list
list3 = list1 + list2
print(list3)

# copy list
list3_copy = list3.copy()
print(list3_copy)

# print list item using while loop
y = 0
while y < len(list1):
    print(list1[y])
    y = y + 1

# print list item using for loop and condition for break
list1 = [1, 8, 9, 82, 56, 'labib', 58, 'apple', 'noman', 'sohan']
print(len(list1))
for i in list1:
    if i == "apple":
        break
    print(i)

# check item in list
print("apple" in list1)

# find item index number
index_apple = list1.index("apple")
print(index_apple)

# remove item
list1.pop(7)
print(list1)
list1.remove("labib")
print(list1)

# add item in list
list1.append("rasel")
print(list1)
