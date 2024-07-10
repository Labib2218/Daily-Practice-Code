# dictionary construction
my_dict = {
    'name': 'Labib',
    'age': 25,
    'city': 'Kushtia',
    'country': 'Bangladesh'
}
print(my_dict)
my_dict2 = dict(name='Imran', age=24, city='Dhaka', country='Bangladesh')
print(my_dict2)
my_dict3 = {'name': 'Habib', 'age': 25, 'city': 'Rangpur', 'country': 'Bangladesh'}
print(my_dict3)

# access item
print(my_dict['name'])
print(my_dict2.get('city'))
print(my_dict2['age'])

# check key in dictionary
if 'labib' in my_dict2:
    print('Yes')
else:
    print('NO')

# check value in dictionary
if 'Labib' in my_dict.values():
    print('This value is available.')
else:
    print(False)

# error handling
try:
    print(my_dict['name1'])
except KeyError:
    print('Error: This key is not available in dictionary.')

# this only show keys
for i in my_dict2:
    print(i)
for i in my_dict2.keys():
    print(i)

# this only show value
for i in my_dict2.values():
    print(i)

# this shows key and value both
for i, j in my_dict.items():
    print(i, ':', j)

# Add item in dictionary
my_dict['email'] = 'taushif4752@gmail.com'
print(my_dict['email'])

# change key value in dictionary
my_dict['email'] = 'labib4752@gmail.com'
print(my_dict['email'])

# delete item from dictionary
print(my_dict2)
my_dict2.pop('name')
print(my_dict2)
del my_dict2['age']
print(my_dict2)

# remove last item
print(my_dict)
my_dict.popitem()
print(my_dict)

# copy dictionary
my_dict_cpy = my_dict.copy()
print(my_dict_cpy)

# update dictionary
# method 1
my_dict_cpy_update = dict(name='Noman', age='26', city='Barisal')
my_dict_cpy.update(my_dict_cpy_update)
print(my_dict_cpy)
# Method 2
my_dict_cpy.update(name="Rasel", age=26, city='Gaibandha')
print(my_dict_cpy)

# change key in dictionary
my_dict3['new_age'] = my_dict3.pop('age')  # this will add new key in the last position
print(my_dict3)
