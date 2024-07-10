# list of square number
# normal code
x_ = []
for i in range(1, 11):
    x_.append(i*i)
print(x_)
# list comprehension
x = [i * i for i in range(1, 11)]
print(x)


# list of qube number
# normal code
x_1 = []
for i in range(1, 10):
    x_1.append(i*i*i)
print(x_1)
# list comprehension
x1 = [i ** 3 for i in range(1, 10)]
print(x1)


# list of normal number
# normal code
x_3 = []
for i in range(1, 11):
    x_3.append(i)
print(x_3)
# list comprehension
x3 = [i for i in range(1, 11)]
print(x3)


# list of even number
# normal code
x_4 = []
for i in range(1, 20):
    if i % 2 == 0:
        x_4.append(i)
print(x_4)
# list comprehension
x4 = [i for i in range(1, 20) if i % 2 == 0]
print(x4)


# list of odd number
# normal code
x_5 = []
for i in range(1, 20):
    if i % 2 != 0:
        x_5.append(i)
print(x_5)
# list comprehension
x5 = [i for i in range(1, 20) if i % 2 != 0]
print(x5)


# list of number where interval is 5
# normal code
x_6 = []
for i in range(1, 101):
    if i % 5 == 0:
        x_6.append(i)
print(x_6)
# list comprehension
x6 = [i for i in range(1, 101) if i % 5 == 0]
print(x6)


# list matrix
# normal code
x_7 = []
for row in range(3):
    a = []
    for col in range(3):
        a.append(row * 3 + col)
    x_7.append(a)
print(x_7)
# list comprehension
x7 = [[row * 3 + col for col in range(3)] for row in range(3)]
print(x7)


# list of tuple
# normal code
x_8 = []
for b in ['a', 'b', 'c']:
    li = []
    for a in [1, 2, 3]:
        y1 = a, b
        li.append(y1)
    x_8.extend(li)
print(x_8)
# list comprehension
x8 = [(a, b) for b in ['a', 'b', 'c'] for a in [1, 2, 3]]
print(x8)


