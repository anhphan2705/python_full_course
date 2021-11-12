#walrus operator :=

#New to Python 3.8
#Assignment expression = walrus operator
#Assigns values to variables as part of a larger expression

#Normal
happy = True
print(happy)

#Walrus Operator = it's assigned and use right in the expression
print(sad := False)

#Normal
foods = list()
while True:
    food = input("What food do you like?")
    if food == "quit":
        break
    foods.append(food)

#Walrus Operator
drinks = list()
while ((food := input("What drink do you like? ")) != ("quit")):
    foods.append(food)