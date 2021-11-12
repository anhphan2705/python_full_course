class Car:

    color = None

class Motorcycle:

    color = None

def change_color(car, color):

    car.color = color

#Creatiing object instances
car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

#Passing a object in as the first argument
change_color(car_1, "blue")
change_color(car_1, "red")
change_color(car_1, "yellow")

change_color(bike_1, "blue")

print(car_1.color)
print(car_2.color)
print(car_3.color)