#method chaining =  calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self
    
    def drive(self):
        print("You drive the car")
        return self
        
    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()

#class.method1().method2() = chaining method. Each method has to return self in order for this to work
car.turn_on().drive()
car.brake().turn_off()

#If the method chaining link is long. It is good practice to out each method on its own line
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off() 