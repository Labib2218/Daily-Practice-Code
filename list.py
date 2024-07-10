# Example of List
list1 = ['banana', 'apple', 'orange']
list2 = [1, 2, 3, 4, 5, 6]
# list3 = [1, 2, 3, True, None, False, 'apple', 'lemon']
# list4 = [1, 1, 5, 88, 88, 'apple', 'apple', 'banana']
#
# # Empty list create
# list5 = []
# print(list5)
# list6 = list()
# print(list6)

# length of list
print(len(list2))

# For loop in list
for i in list2:
    print(i)

for i in range(len(list2)):
    print(i)

# index of list item
print(list2[0])  # first item of list
print(list2[1])  # second item of list
print(list2[-1])  # last item of list

# slicing the list item
print(list2[0:5])  # Here print 0 to 4th index item and 5ht index is exclude
print(list2[2:5])
print(list2[:3])
print(list2[2:])
print(list2[::2])
print(list2[::-1])
print(list2[2::3])

# Add item in list
list2.append(7)
print(list2)
list2.insert(2, 9)
print(list2)

# Remove item in list
list2.pop()
print(list2)
list2.remove(9)
print(list2)
list2.clear()
print(list2)

list7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Reverse list item
list7.reverse()
print(list7)
print(list7[::-1])

# list comprehension

list8 = [i*i for i in list7]
print(list8)
list9 = [i+5 for i in list7]
print(list9)