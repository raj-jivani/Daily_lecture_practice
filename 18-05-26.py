# Operators

# Pythom Operators

# Arithmatic Operators:
    # 1. Addition
    # 2. Substraction
    # 3. Multiplication
    # 4. Divison
    # 5. Modulus
    # 6. Expontiations
    # 7. Floor Divison

# Example

x = 10
y = 20

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)


# Comparision Operator
    # 1. == Equality
    # 2. != not equal
    # 3. < greater than
    # 4. > less than
    # 5. <= greater than equal to
    # 6. >= less than equal to

x = 20
y = 40

print(x == y)
print(x != y)
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)



# Assignment Operator
    # 1. =
    # 2. +=
    # 3. -=
    # 4. *=
    # 5. /=
    # 6. **=
    # 7. //=


x = 10
y = 2

x = y
print(x)

x += y
print(x)

x -= y
print(x)

x *= y 
print(x)

x /= y
print(x)

x **= y
print(x)

x //= y
print(x)


# Logical Operator
    # 1. and
    # 2. or
    # 3. not

# and => return True if both statement are right
# or => return True if one statement right
# not => reverse the result

# check if number is odd or even

num = int(input("Entre number: "))

if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

print("Task END")


# Find the minimum of two numbers

num1 = int(input("Entre number1: "))
num2 = int(input("Entre number2: "))

if num1 > num2:
    print(f"{num2} is minimum number")
else:
    print(f"{num1} is minimum number")

print("Task END")


# Find the largest of three numbers

number1 = int(input("Entre number1: "))
number2 = int(input("Entre number2: "))
number3 = int(input("Entre number3: "))

if number1 >= number2 and number1 >= number3:
    print(f"{number1} is the largest number")
elif number2 >= number1 and number2 >= number3:
    print(f"{number2} is te largest number")
else:
    print(f"{number3} is the largest number")
    
print("Task END")