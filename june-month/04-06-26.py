# Abstraction in OOP.
    # abstraction is the process of hiding implementation details and showing only essential features to the user.
    
    # reduce complexcity
    # increase security
    # improve code re-useability

# an abstract class is a class that can not be instantiend(object can not be created directly)

# Syntax
'''
class Shape(ABC):
    pass

- ABC is a helper class used to make a class abstract
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog Bov Bov")

class Cat(Animal):
    def sound(self):
        print("Cat Meov Meov")

d = Dog()
d.sound()

# you can not create an object of an abstract class

# Abstract class and methods:

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):
    def sound(self):
        print("Dog Bov Bov")

class Cat(Animal):
    def sound(self):
        print("Cat Meov Meov")
        
d = Dog()
c = Cat()

d.sound()
d.sleep()

c.sound()
c.sleep()

# Abstract class Shape() with area

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

r = Rectangle(20,10)
print("Rectangle area:", r.area())
print("Rectangle perimeter:", r.perimeter())

c = Circle(10)
print("Circle area:", c.area())
print("Circle perimeter:", c.perimeter())


# MLModel Abstract class

from abc import ABC, abstractmethod

class MLModel(ABC):
    @abstractmethod
    def train(self):
        pass
    
    @abstractmethod
    def predict(self):
        pass

class LinearRegressionModel(MLModel):
    def train(self):
        print("Training Linear Regression Model")
    
    def predict(self):
        print("Predict using Linear Regression Model")
    
class DecisionTreeModel(MLModel):
    def train(self):
        print("Training Decision Tree Model")
        
    def predict(self):
        print("Pdicting using Decision Tree Model")

l = LinearRegressionModel()
d = DecisionTreeModel()

l.train()
l.predict()

d.train()
d.predict()

