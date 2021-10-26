#import modules
from class_oop import Car

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






