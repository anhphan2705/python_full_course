#Higher Order Function = a function that either
#       1. accepts a function as an argument
#       2. returns a function
#In python, fucntions are also treated as objects

##Example for 1
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

#Passing in a function in order to use it ability
def hello(func):
    text = func("Hello")
    print(text)

#For example, here if loud is passed in, the "hello" will not only be printed, but also in upper case since that is what the loud function does
hello(loud)

##Example for 2
#This is a nested function that will return the inner function
def divisor(x):
    def dividend(y):
        return y/x
    return dividend

#First pass in the argument for the outer function to initialize it
#After this step, the outer functions return the inner function
divide = divisor(2)
#As a result, the inner function is now in place as the outer function
#Here divide is now basically divident(y) instead of divisor(x)
print(divide(10))
