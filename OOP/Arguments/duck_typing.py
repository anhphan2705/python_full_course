#duck typing =  concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               "If it walks like a duck, and it quacks like a duck, then it must be a duck"

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwalking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():
    #anything can be passed in as animals as long as they have the required methods/attributes
    def catch(self, animals):
        duck.walk()
        duck.talk()
        print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

#Because both duck and chicken have walk and talk, it can be pass in to the person.catch()
person.catch(duck)
person.catch(chicken)