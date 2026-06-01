# Python Mutable and Immutable Data types:
   # In python, every value is stored as an object.

# Mutable Objects: Can be change after creation

# Immutable Objects: Can not be change after creation

# Concepts:
    # 1. Memory management
    # 2. Variable behaviour
    # 3. Function Argunments
    # 4. Performance
    # 5. Debugging
    # 6. Learning objectives

# Everything in python as an object

x = 10
name = "python"
numbers = [1, 2, 3, 4]

# Each object has: value, type, memory address

# we can check memory location by using: id() => it is built-in-function in python

x = 10
y = 12

print(id(x))
print(id(y))

# Common immutable types in Python:
    # int 10
    # float 10.4
    # complex 2 + 3j
    # boolean true OR false
    # frozenset frozenset({1,2})
    # bytes b"abcd"
    # tuple (1,2)

x = 10
print("Before:", id(x))

x = x + 1
print("after:", id(x))


# String

a = "python"

# a[0] = "j" # this will give you error because string is an immutable data type

# Common Mutable Types:
    # 1. list [1,2,3]
    # 2. dictionary {"a": 1}
    # 3. set {1,2,3,4}
    # 4. bytearray bytearray(5)


# Mutable List: 

numbers = [1,2,3,4]

print("Before:", numbers)
print("before id:", id(numbers))

numbers.append(5)

print("after:", numbers)
print("after id:", id(numbers))

# Mutable Dictionary

dictionary = {
    "name": "Raj",
    "age": 23
}

dictionary["age"] = 24

print(dictionary)

# String

a_Str = "Hello World"

print(a_Str[3]) # it returns the of that index number
print(a_Str[0:5])  # it returns slice of string by using that index number


# Set Data type
    # they are mutable and new element can be added once sets are defined

basket = {"Apple", "Kiwi", "Orange", "Banana"}

print(basket)

a = set("dfsdhsbsjdskanfjd")
b = set("abdcfehgjiafc")

print(a)
print(b)