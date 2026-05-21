# match-case statement in python
# works similar to switch-case in other programming language

# Syntax
'''
match variable:
    case value1:
        logical code
    case value2:
        logical code
    case _:
        logical code
'''

num1 = 10
num2 = 5

operator = "+"

match operator:
    case "+":
        print(f"Addition: {num1 + num2}")
    case "-":
        print(f"Subtraction: {num1 - num2}")
    case "*":
        print(f"Multiplication: {num1 * num2}")
    case "/":
        print(f"Divison: {num1 / num2}")
    case _:
        print("Invalid Operator")



# Python Loops:

# 1. while loop
# A while loop runs as long as the condition is true

# Syntax
'''
while condition:
    code block
    after thought
'''

i = 1

while i <= 5:
    print(i)
    i += 1


# 2. for loop
# used to iterate: ranges, list, string, tuples, dictionary

# Syntax
'''
for variable in sequence:
    code block
'''

# Print number 1 to 5
for i in range(1,6):
    print(i)

# Loop with String
name = "Pyhton"

for i in name:
    print(i)


# Loop with list
fruits = ["apple", "banana", "mango", "orange"]

for i in fruits:
    print(i)


# Range function
# used to generate sequence of numbers

# range(start, stop, step)
    # start => starting value
    # stop => ending value(excluded)
    # step => increment/decrement


# Example 1:

for i in range(5): # if we give only value then it will be consider as stop value and it takes zero as starting value by default and as same as in step increment by 1 by default
    print(i)

for i in range(1,10):
    print(i)

for i in range(0,15,2):
    print(i)



# Nested Loop
# User for: patterns, tables, matrics, grids
'''
for i in range():
    for j in range():
        code block
'''

for i in range(1,4):
    for j in range(1,4):
        print(j, end=" ")
    print()


for i in range(1,6):
    for j in range(1,11):
        print(i*j, end=" ")
    print()

