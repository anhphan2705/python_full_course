def hello():
    print("Hello")

#If a function is called without (), the memory address of the function on your local memory will be called
print(hello)
#Storing the memory address in a new variable
hi = hello
print(hi)
#If the variable is called with (), the function it assigned to will run
hi()

#Storing print function into say
say = print
#Now say can be used just like print
say("Whooaaaaa")