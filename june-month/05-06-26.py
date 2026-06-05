# Text-File Handleing in Python

# What is file-handling?
'''
- text file handeling in python is the process of creating, opening, reading,
writing, appending and managing text files using python programmes.

- It allows data to be sorted permanently in files instead of temporary memory.
'''

# Defination of Modes of opening File in Python
'''
- Files modes are the different ways used to open a file in python for 
  programming operation like reading, writing, appending or binary handling.
'''

# Defination of I/O operations with Files in Python
'''
-   I/O operations in python are used to be read data from a file and write data into a file.

-   Input operation: Reading data from a file.
-   Output operation: Writing data into a file.
'''

# syntax
'''
    file = open("file_name", "mode")
'''

# Modes
'''
Mode            Meaning
- r     =>      read mode
- w     =>      write mode
- a     =>      append mode(add data at end)
- x     =>      create new file
- rb    =>      read binary file
- wb    =>      write binary file
- r+    =>      read and write
- a+    =>      append and read
'''

# 1. READ mode
    # use to read data from file

file = open("c.txt", "r")
content = file.read()
print(content)
file.close()


# 2. WRITE mode
    # use to write into file

file = open("demo.txt", "w")
file.write("I am learning python")
file.close()

file = open("demo.txt", "r")
content = file.read()
print(content)
file.close()


# 3. APPEND mode
    # use to append data into file.

file = open("demo.txt", "a")
file.write("\n Python is easy to learn")
file.close()


# 4. CREATE mode
    # use to create new file

file = open("a.txt", "x")
file.close()


# I/O operations

# READ files

file = open("demo.txt", "r")
print(file.read())
file.close()


# Output operations

# write text into file

file = open("a.txt", "w")
file.write("\n Hello Python")
file.close()

# write multiple lines

file = open("demo.txt", "w")
lines = [
    "line1 : Python \n",
    "line2 : File-Handling \n",
    "line3 : Easy learning \n"
]

file.writelines(lines)
file.close()


# Using with statement
'''
best method for file handling because file closes automatically.
'''

with open("a.txt", "r") as file:
    content = file.read()
    print(content)


# Binary File Handling
    # used for images, audio, video, etc.......

file = open("01-06-26.py", "rb")
content = file.read()
print(content)
file.close()

# Read and write binary file(r+)
file = open("a.txt", "r+")
print(file.read())
file.write("Python file handling")
file.close()

# create and read file

file = open("b.txt", "w")
file.write("Hello, Welcome to python class")
file.close()

file = open("b.txt", "r")
print(file.read())
file.close()