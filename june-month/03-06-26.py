# Object ORianted Programming (OOP):
    # OOP is a programming paradigm that organize code using classes and objects. it helps in creating reusable, maintable and scalbale application.

# 1. Class and Object
    # a class is a blueprint or template for creating object.
    # an object is instance of class.

# syntax
'''
class class_name:
    pass

obj = class_name()    
'''

# Student class

class Student:
    def __init__(self, name, age):  # This is call constructer
        self.name = name
        self.age = age
    
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating object

s1 = Student("Raj", 23)
s2 = Student("Hiren", 23)

s1.display()
s2.display()

# self keyword
    # self represent that current object of th class.

# Instance method
# Instance variables

# Employee class

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show(self):
        print("Employee name:", self.name)
        print("Employee salary:", self.salary)

e1 = Employee("Sahaj", 100000)
e2 = Employee("Vandan", 50000)

e1.show()
e2.show()

# del keyword
    # delete variable
    # delete objects
    # delete object properties

x = 100
print(x)

del x
print(x)

# Student class

class Stu:
    def __init__(self):
        self.name = "Raj"

stu1 = Stu()
print(stu1.name)

del stu1.name
print(stu1.name)


# 1. Encapsulation
    # Encapsulation mean wrapping object(data) and function(methods) into a single unit(class) and restricting direct access to some data.

# Uses:
    # Public
    # Protected
    # Private

# Bank Account 

class BankAccount:
    def __init__(self):
        self.__balance = 100000
    
    def depoiste(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__balance -= amount
    
    def getBalance(self):
        return self.__balance

account1 = BankAccount()
print("Account Balance:", account1.getBalance())

account1.depoiste(50000)
print(account1.getBalance())

account1.withdraw(20000)
print(account1.getBalance)


# 2. Polymorphism:
    # Polymorphism mean one interface, many forms
    
# The same method behaves differently for different object
# Method overriding

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog Bow Bow")

class Snake(Animal):
    def sound(self):
        print("Snake Shhhhh.....")

d = Dog()
s = Snake()

d.sound()
s.sound()

# same function different objects

class Car:
    def move(self):
        print("Car is moving")

class Plane:
    def move(self):
        print("Plane id flying")

def action(vehicle):
    vehicle.move()
    
c = Car()
p = Plane()

action(c)
action(p)


# 3. Abstaraction
    # abstraction mean hiding implementation details and showing only essential features.
    # python provides abstraction using the abc module

# Vehicle class

class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

c = Car()
b = Bike()

c.start()
b.start()


# 4. Inheritance
    # inheritance mean allows one class to accquire properties and methods of another class
    
    
    # 1.Single Inhritance

class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    pass

c = Child()

c.show()

    # 2. Multi-level inheritance

class GrandParent:
    def title(self):
        print("Grand Parent")

class Parent(GrandParent):
    def title1(self):
        print("Parent")

class Child(Parent):
    def title2(self):
        print("child")

obj = Child()

obj.title()
obj.title1()
obj.title2()

    # 3. Multiple Inheritance

class Father:
    def father_property(self):
        print("Car")

class Mother:
    def mother_property(self):
        print("Jwelary")

class Child(Father, Mother):
    pass

c = Child()

c.father_property()
c.mother_property()

    # 4. Hireachical Inheritance

class Parent:
    def display(self):
        print("Parent class")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()

c1.display()
c2.display()

    # 5. Hybrid Inheritance
    
class A:
    def showA(self):
        print("A class")

class B(A):
    def showB(self):
        print("Class B")

class C(A):
    def showC(self):
        print("Class C")
        
class D(B, C):
    def showD(self):
        print("Class D")

z = D()

z.showA()
z.showB()
z.showC()
z.showD()