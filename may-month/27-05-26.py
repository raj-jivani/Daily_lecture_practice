# Stirng Formatting

name = "Aisha"
age = 21

# using f-string
print(f"My nae is {name} amd I am {age} years old.")

# using in-built-function .format()
print("My name is {} and I am {} years old.".format(name, age))

# using % formatting
print("My name is %s and I am %d years old."%(name, age))

price = 199.456
print(f"Price {price:.2f}")

# Lsit and Tuples (Mutability)

my_list = [10, 20, 30]
print(my_list)

my_list[1] = 200
print("After update:", my_list)

# Methods of list

my_list.append(50)
print(my_list)  # it will add this value in last in list

my_list.remove(10)
print(my_list) # it will remove that value from list

# Tupples

tuple = (10,20,30,40)
print(tuple)


# Indexing and Slicing

text = "Python"

# indexing
print(text[2])
print(text[len(text) - 1])
print(text[-1])

# slicing
print(text[0:3])
print(text[3:])
print(text[-3:])

# reverse string
print(text[::-1])

# Using list with Slicing and Formatting

students = ["Dixit", "Jinal", "Raj", "Janvi", "Jiya", "Rutva"]

print(students)
print("First Three Students:", students[:3])

# loop

for i in students:
    print(f"Welcome {i}")

# length
print("Length of list:", len(students))

# checking element
print("Is Jiya Present", "Jiya" in students)

# Nested List

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)

# Accessing element
print("Middle Element:", matrix[1][1])


# String Methods

message = "Python Programming"

print("uppercase message:", message.upper())
print("capitalize message:", message.capitalize())
print("replace message:", message.replace("Python", "AI/ML"))
print("split message:", message.split())


# List methods

numbers = [2,5,4,7,9,8]

numbers.sort()
print("shorted list:", numbers)

numbers.reverse()
print("reverse list:", numbers)

numbers.insert(1,100)
print("after insert:", numbers)