#scope =    The region that a variable is recognized
#           A variable is only available from inside the region it is created
#           A global and locally scpaed versions of a variable can be created

name = "Anh"        #Global scope (available insde & outside function)

def display_name():
    name = "Anh"    #Local scope (only available only inside this function)
    print(name)

display_name()
print(name)

#Order of using variable: Local - Enclosing - Global - Built-in