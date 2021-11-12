#Prevent a user from creating an object of that class
#   + compels a user to override abstract methods in a child class

#Abstract class = a class which contains one or more abstract methods
#Abstract method = a method that has a declaration but does not have an implementation

#abc is shorten for abstract class
from abc import ABC, abstractmethod

class Vehicle(ABC):

    #Add a decoration @abstractmethod for good practice of marking abstract method
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop():
        print("You stop the motorcycle")

vehicle = Vehicle()
car  = Car()
motorcycle = Motorcycle()

vehicle.go()
car.go()
motorcycle.go()
