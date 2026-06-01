# Python Data Types

# Frozen Sets:- They are immutable and new element can not added after its defined

fs = frozenset("hellopython")
print(fs)

cities = frozenset(["surat", "ahemedabad", "vadodara", "pune", "mumbai"])
print(cities)


# Number Data types in Python

# Number have four type in python:
    # 1. integer
    # 2. float
    # 3. complex
    # 4. long number
   
int_num = 10
float_num = 120.12
# complex_num = 2i +3j
# long_num = 23234234L

print(int_num)
print(float_num)


# List data types in python

# A list contains items seperated by commas and enclosed within brackets[]. list is similar to array in c programming.
# But diffrence is that all the items belonging to a list can be diffrent data types.

list = [1, "Raj", 3.14, True]
print(list)

list1 = ["Hello", "World"]
print(list1)

print(list[0:1])  # it slice list and return new list
print(list * 2)  # it gives all values twice
print(list + list1) # it concatinates both list



# Dictionary data types in python

# Dictionary consists of key-value pairs. It is enclosed with by curely braces{} and values can be using by square brackets[].

dictionary = {
    "name": "Raj Jivani",
    "age": 23
}

print(dictionary)
print(dictionary["age"]) # it returns the value of that key which you mention in square bracket
print(dictionary.values())  # it returns all values of dictionary
print(dictionary.keys())  # it returns all keys of dictionary


# Tuples Data type in Python

# list are enclosed with brackets[] where tuple are enclosed with parentheses() and can not be update beacuse it is immutable

tuple = (0, "Raj", 3.14, False)
print(tuple)
print(tuple[1])

tuple1 = ("Python")

# print(tuple + tuple1) # it will not be concatinate and returns an error

# tuple1[1] = "World"
# print(tuple1)  # it returns an error becuase tuple is immutable data type


# Python Operators
    # 1. Arithmatic "+, -, *, /, %"
    # 2. Assignment "=, +=, -=, *="
    # 3. Comparision "==, !=, <, >, <=, >="
    # 4. Logical "and or not"
    # 5. Identity "is, is not"
    # 6. Membership "in, not in"
    # 7. Bitwise "&, ^"