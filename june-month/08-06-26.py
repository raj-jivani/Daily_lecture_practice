# Exception handeling in Python.

'''
An exception is an error that occurs during programme executing. if an Exception is not handled,
the programme stop immediately.
'''
print(10/0)

# to avoid programme crashes, Python provides exception handeling using:
'''
try
catch
else
finally
'''

# 1. try.....except
    # used to handle errors safely

# syntax
'''
try:
    # code block
except:
    # error handling code
'''

try:
    num = int(input("Enter number: "))
except ZeroDivisionError:
    print("can not divide by zero")
except ValueError:
    print("Invalid Input")


# 2. try.....except.....else
    # else block executes only when no exception occurs


# syntax
'''
try:
    # code block
except:
    # error handling code
# else:
    exicutes if no error
'''

try:
    num = int(input("Enter number:"))
    result = 10/num
except ZeroDivisionError:
    print("Can not divide by zero")
else:
    print(result)



# 3. try.....except.....finally
    # finally block always execute whether error occurs or not

# syntax
'''
try:
except:
finally:
'''

try:
    file = open("demo.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not Found")
finally:
    print("Programme finished")


# 4. try.....except.....else.....finally
    # combination of all blocks

try:
    num = int(input("Enter number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Can not divide by zero")
else:
    print(result)
finally:
    print("Programme finished")


# Important Exception types in Python:
'''
    1. ZeroDivisionError
    2. TypeError
    3. ValueError
    4. IndexError
    5. KeyError
    6. FileNotFoundError
'''

# Advantages
'''
    - prevent programme crash
    - improve programme realiability
    - makes debugging easier
    - handles unexpected errors gracefully
'''

try:
    atm_pin = int(input("Enter ATM pin: "))
except ValueError:
    print("PIN must contain numbers only")
else:
    print(atm_pin)
    print("PIN accepted")