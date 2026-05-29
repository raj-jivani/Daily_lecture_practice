# Functions in Python

# Functions, Recursion, Lambda Function, Global-keyword and multiple return value

# What is Function?
    # Functions are reusable block of code used to perform a specific task
    # Reusability, cleaner code, better optimization, reduce repetition

# Type of Functions:
    # Built in Function
    # User DEfine Function (UDF)

def add():
    print("Welcome Student")
add()

def multiply(a,b):
    print("Multiplication", a * b)
multiply(4,5)


# Recursion Function
    # a function calling itself
    # factorial, fibonacci, tree structure, problem solving
    
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# 2. Sum of two numbers

def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

print(total(5))


# 3. Anonymous Function / Lambda

# syntax
''' lambda arguments: expression '''

square = lambda x: x * x
print(square(2))

add = lambda a,b: a + b
print(add(2,3))

# list

numbers = [1,2,3,4,5]

result = list(map(lambda x: x * 2, numbers))
print(result)

# filter

numbers = [1,2,3,4,5,6,7,8,9,10]

odd = list(filter(lambda x: x%2 != 0, numbers))
print(odd)

# Normal Function
'''
    def keyword
    multiple value
    named
'''

# Lambda Function
'''
    lambda keyword
    single line
    unonymous
'''

# Global Keyword
    # variable created outside function are called global variables
    # to modify global variable inside function use "global"

x = 10
def show():
    print(x)
show()

count = 0

def increment():
    global count
    count += 1

increment()
print(count)


# Return Multiple value
    # python function can return multiple value:
        # single value
        # multiple value

def calculation(a,b):
    return a+b, a-b

result = calculation(10,5)
print(result)


def student_info():
    name = "Raj Jivani"
    marks = 90
    return name, marks

n, m = student_info()
print(n ,m)

# returning multiple calculation
# returning user data
# returning API response


# Built in functions

numbers = [1,2,3,4,5]

print("Length:", len(numbers))
print("max num:", max(numbers))
print("min num:", min(numbers))
# this are pre defined functions inside pyhton. you don't need to create them.


# User defined Function (UDF)
def greet(name):
    print(f"Hello, {name}.")
greet("Raj")


# Arbitary Arguments(*args)

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1,2,3,4,5))
# *args collects multiple value in tuple


# Key-word Arguments(**kwargs)
    # when passing named values

def student_info(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)

student_info(name="Raj Jivani", age = 23, course = "Python")
# **kwargs stored data in dictionary


# doc (Documentation String)
# used to describe function

def multiplication(a,b):
    """"This function returns the multiplication of two values"""
    return a*b

print(multiplication(4,5))
print(multiplication.__doc__)



# TNRN classification
'''
    T => take arguments
    N => no arguments
    R => return value
    N => no value
'''

# classfication
'''
    TNRN => take no arguments, return no value
    TSRN => take some arguments, return no value
    TNRS => take no arguments, return some value
    TSRS => take some arguments, return some value
'''

# 1. TNRN
'''
    NO PARAMETER, NO RETURN STATEMENT
'''

def greet():
    print("Hello Students")
greet()


# 2. TSRN
'''
    TAKE PARAMETER, RETURN NO VALUE
'''

def add(a,b):
    print("Addition:", a+b)
add(2,3)


# 3. TNRS
'''
    NO PARAMETER, RETURN VALUE USING return
'''

def message():
    return "Hello Guys"
print(message())


# 4. TSRS
'''
    ACCEPT PARAMETER,
    RETURN OUTPUT
'''

def multiply(a,b):
    return a*b
print(multiply(4,5))