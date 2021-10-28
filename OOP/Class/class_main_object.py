#import modules
#from module import class
from class_variable import Car

#class_name(attributes = values) = making an object
porsche = Car(make = "Porsche", model = "911", year = "1969", color = "red") 
mustang = Car("Ford", "Mustang", 2022, "red")

#object.attributes = Accessing object's attributes
print(porsche.make)
print(porsche.model)
print(porsche.year)
print(mustang.color)

#object.method = Accessing object's methods
porsche.stop()
mustang.drive()

#the object variables can be changed outside the class
#only the object variable is changed, other object var stays the same
#if class variable is changed, then all object will have the changed variable unless alternated otherwise
mustang.wheels = 2
print(mustang.wheels)
print(porsche.wheels)






