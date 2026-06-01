# create 1D array with 5 integer element. Display using loop.

list_1 = [1,2,3,4,5]

for i in list_1:
    print(i)

# write a programme to find the length of a 1D array without using built in function.

a = []

size = int(input("Size of array: "))

for i in range(size):
    value = int(input(f"a[{i}] = "))
    a.append(value)

count = 0

for i in a:
    count += 1

print("Lenght of Array:", count)

# write a programme to find the sum and average of of 1D array without using built in function

b = []

sIZe = int(input("Entre array size: "))

for i in range(sIZe):
    valUe = int(input(f"a[{i}] = "))
    b.append(valUe)

total = 0
couNt = 0

for i in b:
    total += i
    count += 1

print("Sum of aaray: ", total)
print("Avaerage of array: ", total / couNt)

# write a programme to perform addition operation of two 1d arrays and store in another array

c = []
d = []
e =[]

sIZE = int(input("Entre size of array: "))

for i in range(sIZE):
    val = int(input(f"a[{i}] = "))
    c.append(val)

for i in range(sIZE):
    v = int(input(f"a[{i}] = "))
    d.append(v)

for i in range(sIZE):
    e.append(c[i] + d[i])

print(e)


# write a programme of an array from 1 to 10

f = []

for i in range(1,11):
    f.append(i)

print(f)


# Take user input for a number and check if it exists in Array

li_1 = [12, 34, 55, 70, 65, 45]

guess_number = int(input("Enter number: "))

guess = guess_number in li_1

if guess == True:
    print("Number found at index:", li_1.index(guess_number))
else:
    print("Not FOUND")


# Print all the even numbers from the array

array_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in array_1:
    if i % 2 == 0 :
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")


# print the first, middle amd middle element in array

arr = [2.56,45,3,66,67,33,23]

print("First ele:", arr[0])
print("Middle ele:", arr[len(arr) / 2])
print("Last ele:", arr[-1])


# 2D array
    # Array inside another array
    # it stored data in rows and columns
    # it looks like a table or matrix

# Example

arr_2d = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# accessing element in 2D array:
    # arr[row][column]

print(arr_2d[0][0])
print(arr_2d[2][2])

# taske input in 2d array

array1 = []

rows = int(input("Enter size of rows: "))
columns = int(input("Enter size pf columns: "))

for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input(f"a[{i}][{j}] = "))
        row.append(value)
    array1.append(row)

print(array1)


# Print 2D array using nested loop

aa = [
    [1,2],
    [3,4]
]

total = 0

for i in aa:
    for j in i:
        total += j

print("Total:", total)

# sorting collection data types

# arranging data in order
    # assending
    # descending

# sort() method

numbers = [1,8,5,2,9,4]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

fruits = ["mango","banana", "orange", "apple"]

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

