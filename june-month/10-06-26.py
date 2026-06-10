# Polymorphism
'''
    - In python, polymorphism allows the same method name to perform different task depending on the object or situation.
'''
# Two Types:
    # 1. method overloading
    # 2. method overrriding

# method overloading mean creating multiple method with same name but different parameter.
# python do not support traditional overloading directly, but it can be achieved using default parameter.

class Calculator:
    def add(self, a, b, c):
        return a + b + c

obj = Calculator()

print(obj.add(10,20,0))
print(obj.add(10,20,30))


# 2. Method Overriding
    # method overriding occurs when a child class providers a different implementation of a method already defined in the parent class.

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog sound")

obj = Dog()
print(obj.sound())

# dog class overrides the sound method of animal class. Child class method is exicuted instead of parent class.


# issubclass()
'''
issubclass() is built in function in pyhton to check whether one class is a subclass of another class.
'''

# syntax
'''
issubclass(child_class, parent_class)
Return True or False
'''

class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))



# super() keyword
'''
- super() is used to call method or constructer of the parent class from the child class.
- it helps in reusing parent class code.
'''

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks
    
    def dispaly(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

obj = Student("Raj", 98)

obj.dispaly()


# 1. Using super() with constructer

class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructer")

object = Child()


# 2. Access Parent class method

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog makes sound")

d = Dog()
d.sound()

# 3. Parent class and Child class both have variable

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def dispaly(self):
        print(f"Name: {self.name}")

a = Student("Raj")
a.dispaly()