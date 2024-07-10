# tuple
Tuple = ('Banana', 'Apple', 'Carry', 'Orange', 'Mango')
print(Tuple)

# access using index number
print(Tuple[2])
print(Tuple[-1])

# slicing tuple
print(Tuple[0:5])
print(Tuple[:5])
print(Tuple[0:])
print(Tuple[::2])
print(Tuple[::-1])

# add item in tuple
h = list(Tuple)
h.append('Olive')
h.insert(3, 'Kiwi')
Tuple = tuple(h)
print(Tuple)

# access item using for loop
for i in Tuple:
    print(i)

# check item
if 'Apple' in Tuple:
    print('Yes')
else:
    print('No')

# multiply tuple item
tup = Tuple * 5
print(tup)

# count tuple item
a = tup.count("Apple")
print(a)

# find index of an item
b = tup.index("Apple")
print(b)

# join tuple
my_tuple = (1, 4, 25, 2, 8)
x = my_tuple + Tuple
print(x)

# unpack tuple
print('\nunpack tuple')
my_tuple2 = ('Labib', 'Mojo', 'Pink', 'Beef', 'Carry', 'Kiwi', 'Orange', 'Mango')
human, cola, color, meat, *fruit = my_tuple2
print(human, color)
print(fruit)

