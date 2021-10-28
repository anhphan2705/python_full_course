#inheritance =  classes can inherits attributes and methods from another class
#               these classes can form a parent-child relationship
#               the child class will receive everything that the parent class has

class Animal:
    alive =True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

#It is better practice to have 1 class per module (file)

#class ChildClass(ParentClass): = delaring a child class by passing the parent class as a parameter
class Rabbit(Animal):
    def jump(self):
        print("This animal is jumping")

class Fish(Animal):
    def swim(self):
        print("This animal is swimming")

class Bird(Animal):
    def fly(self):
        print("This animal is flying")

rabbit = Rabbit() #Each time a class is called. It will run the class's constructor
fish = Fish()
bird = Bird()

#Accessing parent's variable
print(rabbit.alive)

#Accessing parent's method
print(bird.eat())
print(fish.sleep())

#Accessing child class internal method/attribute. Other child classes that use the same parent class can't see this
print(fish.swim())
print(rabbit.jump())
print(bird.fly())


