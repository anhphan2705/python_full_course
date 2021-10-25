#*args = parameter that will pacl all arguments into a tuple
#       useful so that a function can accept a varying amount of arguments

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for num in stuff:
        sum += num
    return sum
print(add(1, 2))

#You cant change the args since it is a tuple. You have to convert it into a list to alternate values