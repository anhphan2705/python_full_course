#Multi-level inheritance = when a derived (child) class inherits another derived (child) class inherits another derieved (child) class

#(Class 1) Parent class
class Organism():
    alive = True

#(Class 2) A child class of parent class (Class 1). Inherits everything from (Class 1)
class Animal(Organism):
    def eat(self):
        print("This animal is eating")

#(Class 3) A child class of parent class (Class 2). Inherits everything from (Class 2) and (Class 2)'s parent class which is (Class 1)
class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()

#Accessing (Class 1)'s variable
print(dog.alive)
#Accessing (Class 2)'s variable
print(dog.eat())
#Accessing its own variable
print(dog.bark())