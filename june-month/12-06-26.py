# Pyhton Modeuls And Function----------------

# 1. ----------- Math Module-----------------
    # math module is use for mathmetical calculation.

import math

print("\n ========== Math Module ==========")

# 1. sqrt()
    # sqrt() is used to find the square root of a number.

# syntax
'''
    math.sqrt(number)
'''
number = 36
print(math.sqrt(number))


# 2. pow()
    # pow() is used to calculate power.

base = 2
power = 5

result = math.pow(base, power)
print(result)


# 3. ceil()
    # rounds the number up to nearest integer.

number = 4.2
result = math.ceil(number)
print(result)


# 4. floor()
    # floor() rounds the number Down to the nearest integer.

number = 4.9
result = math.floor(number)
print(result)


# 5. factorial()
    # factorial() calcualte factorial of given number

print(math.factorial(5))


# 6. gcd()
    # gcd() finds greatest common divisor.

num1 = 18
num2 = 12

result = math.gcd(num1, num2)
print(result)


# 7. sin()
    # sin() calculate sine value.

result = math.sin(0)
print(result)


# 8. cos()
    # cos() calcualtes cosine value.

result = math.cos(1)
print(result)


# 9. tan()
    # tan() calcualtes tangent value.
    
result = math.tan(1)
print(result)


# 10. log()
    # log() calcualte logarithm value.

result = math.log(10)
print(result)


# 11. PI
print(math.pi)

# 12. e
    # math.e give Euler's number.

print(math.e)



# 2. ----------- Random Module-----------------
'''
    - random module is used to generate random values.
    - it is useful for games, otp generate, password generation, random selection and many more applications.
'''

import random

print("\n ========== Random Module ==========")

# 1. randint()
    # randint() generate a random integer between two numbers.

# syntax
'''
    random.randint(start, end)
'''
result = random.randint(1, 10)
print(result)


# 2. random()
    # random() generate a random float number

# syntax
'''
    random.random()
'''

result = random.random()
print(result)


# 3. choice()
    # choice() select random item from a list.

# syntax
'''
    random.choice(list)
'''
colors = ['blue', 'orange', 'brown', 'green', 'red', 'yellow']

result = random.choice(colors)
print(result)


# 4. shuffle()
    # shuffle() mixes the element of list.

# syntax
'''
    random.shuffle()
'''

list = [1,2,3,4,5,6,7,8,9,10]
print(list)

random.shuffle(list)
print(list)


# 5. uniform()
    # uniform() generate a random decimal number between two values.

# syntax
'''
    random.uniform(start, end)
'''

result = random.uniform(1, 100)
print(result)



# 6. randrange()
    # randrange() generate a random number from a given range.

# syntax
'''
    random.randrange(start, stop, step)
'''

result = random.randrange(1, 20, 2)
print(result)



# 7. sample()
    # sample() selects multiple unique random items.

# syntax
'''
    random.sample(list, count)
'''

numbers = [10,20,30,40,50,60,70,80,90,100]

result = random.sample(numbers, 2)
print(result)



# 3. ----------- UUID Module-----------------
'''
    - uuid generate unique id.
    - uuid() genrate multiple unique id.
    - using current time and IP/MAC address.
'''

import uuid

print("\n ========== UUID Module ==========")

# 1. uuid1()

result = uuid.uuid1()
print(result)


# 2. uuid4()
    # uuid4() generate a random unique ID.

result = uuid.uuid4()
print(result)


# 3. uuid3()
    # uuid3() generate with namespace, name.

result = uuid.uuid3(uuid.NAMESPACE_DNS, "example.com")
print(result)

# 4. uuid5()

result = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
print(result)