#class class_name: = how to create a class
class Car:

    wheels = 4  #class variable  

#Constructor method = declare and assign value to attributes
    def __init__(self, make, model, year, color):
        self.make = make        #this is intance variable
        self.model = model
        self.year = year
        self.color = color
#Methods
#You will have to put self as the first parameter. However, it will not require any imput. Basically a placeholder saying I belong to whatever scope they r in
    def drive(self):
        print(f"This {self.model} is driving")

    def stop(self):
        print(f"This {self.model} is stopped")
