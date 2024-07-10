# import pprint
# This is list comprehension
print('...........This is List Comprehension..............')
# Normal code
value = []
for i in range(10):
    value.append(i)
print(value)

# Comprehension Code
value_n = [i for i in range(10)]
print(value_n)

# Normal code
evens = []
for i in range(50):
    is_even = i % 2
    # is_even = i % 2 == 0
    # if is_even:
    if is_even == 0:
        evens.append(i)
print(evens)

# Normal code
evens2 = []
for i in range(0, 50, 2):
    evens2.append(i)
print(evens2)

# Comprehension Code
evens_c = [i for i in range(0, 50, 2)]
print(evens_c)
evens_c2 = [num for num in range(50) if num % 2 == 0]
print(evens_c2)

# Normal code
option = ['any', 'apply', 'a', 'axe', 'angry', 'albany', 'banyan', 'world', '', 'apex']
ay_list = []
for word in option:
    if len(word) <= 1:
        continue
    elif word[0] != 'a':
        continue
    elif word[-1] != 'y':
        continue
    ay_list.append(word)
print(ay_list)

# Comprehension Code
ay_list_c = [word for word in option if len(word) >= 1 if word[0] == 'a' if word[-1] == 'y']
print(ay_list_c)

# Normal Code
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13]]
flatten = []
for i in matrix:
    for j in i:
        flatten.append(j)
print(flatten)

# Comprehension Code
flatten_c = [j for i in matrix for j in i]
print(flatten_c)

# Normal Code
category = []
for i in range(20):
    if i % 2 == 0:
        category.append('Even')
    else:
        category.append('Odd')
print(category)

# Comprehension Code
category_c = ['Even' if i % 2 == 0 else 'Odd' for i in range(20)]
print(category_c)

# Normal Code
# printer = pprint.PrettyPrinter()
l1 = []
for i in range(5):
    l2 = []
    for j in range(5):
        l3 = []
        for k in range(5):
            l3.append(k)
        l2.append(l3)
    l1.append(l2)
# printer.pprint(l1)
print(l1)

# Comprehension Code
l1_c = [[[i for i in range(5)] for _ in range(5)] for _ in range(5)]
print(l1_c)


# Normal Code
def square(x):
    return x ** 2


squ_list = []
for i in range(10):
    squ_list.append(square(i))

print(squ_list)

# Comprehension Code
squ_list_c = [square(i) for i in range(10)]
print(squ_list_c)

squ_list_c1 = [i*i for i in range(10)]
print(squ_list_c1)

# This is Dictionary comprehension
print('...........This is Dictionary Comprehension..............')

# Normal Code
my_dict = {}
pairs = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
for i, j in pairs:
    my_dict[i] = j
print(my_dict)

# Comprehension Code
my_dict_c = {i: j for i, j in pairs}
print(my_dict_c)

