import time

start = time.time()

i = 0
while i <= 5:
    time.sleep(1)
    print(i)
    i += 1

# summation using loop
sum1 = 0
for i in range(1, 101):
    sum1 = sum1 + i
    i += 1
print(sum1)

# printing same thing over and over using while loop
j = 1
while j < 10:
    time.sleep(1)
    print("Learn with Labib")
    j = j + 1

n = 5
message = 'Why so serious?'
for i in range(n):
    time.sleep(1)
    print(message)

# make list using for loop
my_list = []
for i in range(1, 11):
    my_list.append(i)
print(my_list)


end = time.time()
time_need = end - start
print(f"Total time need here is: {time_need / 60} minutes")
