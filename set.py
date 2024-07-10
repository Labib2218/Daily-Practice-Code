# set construction
# set does not allow same item multiple times. So it can print one time each item
my_set1 = {"apple", "banana", "cherry", "apple"}
print(my_set1)
x = (2, 4, 5, 86, 6, 8, 9)  # convert tuple into set. we can also convert list into set
my_set2 = set(x)
print(my_set2)

# add new item into set
list1 = list(my_set1)  # convert set into list
print(list1)
list1.append("mango")
print(list1)
my_set1 = set(list1)  # then convert into set
print(my_set1)

my_set1.add("kiwi")
print(my_set1)


# check set item:
if 'applee' in my_set1:
    print('Yes')
else:
    print('No')

print('mango' in my_set1)
print('banana' not in my_set1)

# Access Set item
for i in my_set1:
    print(i)


# update set
my_set2 = {"pineapple", "mango", "papaya"}
my_set1.update(my_set2)
print(my_set1)

# add a list with set
my_set1.update(list1)
print(my_set1)

# Remove set item
my_set1.remove("apple")
print(my_set1)

# Join item in set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = [9, 7, 0]
set4 = (89, 58, 65)

set1.update(set2, set3, set4)
print(set1)

# Copy set item
set5 = set1.copy()
print(set5)
