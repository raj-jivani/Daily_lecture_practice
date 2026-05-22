# Break Statement
# Stops the loop immidiately

for i in range(1,6):
    if i == 4:
        break
    print(i)

# Continue Statement

for i in range(1,7):
    if i == 3:
        continue
    print(i)

# Pass Statement
for i in range(1,7):
    if i == 3:
        pass  # Null Statement(Does nothing)
    print(i)


# Patterns in Pyhton

# Right angle triangle
for i in range(1,6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()


# Number Triangle
for i in range(1,6):
    for j in range(i):
        print(i, end=" ")
    print()

# Pyramid
row = int(input("Entre number of rows"))

for i in range(1, row+1):
    for j in range(row-1):
        print(" ", end=" ")
    for j in range(2*i-1):
        print("*", end=" ")
    print()


# Inverted Triangle
for i in range(6,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()


# Floyd's Triangle

num = 1

for i in range(1,6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


# else with loops
# the else block runs when loops finishes normally

for i in range(5):
    print(i)
else:
    print("Loop finished")

# break

for i in range(5):
    if i == 3:
        break
else:
    print("Loop finished")
# here else will not work because loop stopped using break statement


# List & Tuples

my_list = [12, 34, 55, 78]
print(my_list)

my_list[0] = 52
print(my_list)


# Tuples in Python

tuple = (14,20,12,23)
print(tuple)

tuple[0] = 11 # this will give you error because tupple is immutable data type