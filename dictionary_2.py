# nested dictionary
biodata = {
    "address": {
        "village": "Satirzan",
        "post": "Mojumdarhat",
        "upzilla": "Sundargonj",
        "zilla": "Gaibandha",
        "division": "Rangpur"
    },
    "name": "Md Taushif Imran Labib",
    "roll": 191010,
    "registration": 225,
    "session": "2019-20",
    "dept.": "Geography and Environment",
    "degree": "BSc",
    "institution": "Islamic University,Kushtia-7003"
}
my_family = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(biodata)
print(my_family)

# print all the key using for loop
for i in biodata:
    print(i)

# length of dictionary
print(len(biodata))

# access item from dictionary
print(biodata["name"])
print(biodata["address"]["zilla"])  # access from nested dictionary

# convert dictionary to list
my_list = list(biodata)
print(my_list)

# change key value
biodata["roll"] = 191009
print(biodata)

# print key and values using for loop
for key, value in biodata.items():
    print(f"{key} : {value}")

print()

# print all value using for loop
# method 1
for x in biodata:
    print(biodata[x])

# method 2
for i in biodata.values():
    print(i)

# print key and value from nested dictionary
for f, obj in my_family.items():
    print(f)
    for j in obj:
        print(j, ':', obj[j])

