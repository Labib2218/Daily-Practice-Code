import random


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(7, 8, 5, 8))


def random_roll(length=10):
    roll = []
    for i in range(length):
        i = random.randint(1, 55)
        if i in roll:
            pass
        else:
            roll.append(i)
    return roll


print(random_roll())

def sumation(a, b, c):
    sum = a + b + c
    print(sum)


sumation(245, 425, 243)
sumation(25, 485, 2423)
sumation(2455, 45, 2343)
sumation(255, 495, 24003)

j = lambda x, y: x * y
print(j(25, 89))
