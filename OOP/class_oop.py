#class class_name: = how to create a class
class Car:

#Constructor method = declare and assign value to attributes
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
#Methods
    def drive(self):
        print(f"This {self.model} is driving")

    def stop(self):
        print(f"This {self.model} is stopped")
