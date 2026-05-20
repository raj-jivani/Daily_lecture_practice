# Identity Operator in Python

# Identity Operator check whether two variables point to the same object in memory.

# is returns True if both variables refer to the same object.
# is not returns True if both variables refer to diffrent object

a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)
print(a is not c)

# Explanation
# a and b refer to the same list object
# c has the same value but is a different object in memory



# Membership Operator in Pyhton
# Membership operator check whether a value exists in a sequence like list, tuple, string or dictionary.

# in returns True if value exists.
# not in returns True if value does not exists

numbers = [1,2,3,4]

print(2 in numbers)
print(5 in numbers)
print(2 not in numbers)
print(5 not in numbers)

text = "pyhton"
print("py" in text)
print("Py" in text)



# Bitwise Operator in Python

# Bitwise operator work on binary numbers(bits)

# & => Bitwise AND
# ^ => Bitwise XOR

# Bitwise AND

a = 5
b = 3
print(a & b)

a = 5
b = 3
print(a ^ b)


# Python Control Flow
    # Condition Statements => allow a programme to make decisions based on conditions

# if, elif, else

# if statement
# The if statement allow a programme to check whether a condition is True

# syntax
'''
if condition:
do something
'''

age = 18

if age >= 18:
    print("You are eligible to vote")

# if...else statement
# Use it when you want two possible outcome.

#syntax
''' if (condition):
        do something
    else:
        do something
'''

number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# if...elif...else
'''if(condition):
        do something
    elif(condition):
        do something
    else:
        do something
'''

marks = 70

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

