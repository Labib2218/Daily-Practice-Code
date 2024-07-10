# list matrix
list_matrix = [
    [1, 2, 3, 4, 5, 6, 7],
    [5, 9, 68, 5, 64, 3, 5],
    10, 2
]
print(list_matrix)

# access item
i = list_matrix[1][4]
print(i)

# add item
list_matrix.append([20, 58, 65, 30])
print(list_matrix)

# change the value
list_matrix[1][2] = 98
print(list_matrix)

# remove item
list_matrix.pop(3)
print(list_matrix)

# length of list
print(len(list_matrix))

# convert list into tuple
my_tuple = tuple(list_matrix)
print(my_tuple)


