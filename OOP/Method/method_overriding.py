#Method overriding = an ability of object oriented programming to allow a subclass (child class) to provide a specific implementation method that is already provided by its parent class  

class Animal:

    def eat(self):
        print("This annimal eats grass")

class Rabbit(Animal):
    
    #This is a method that have the same name as the method in the parent class to override it
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()