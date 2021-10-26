#**kwargs = parameter that will pack all arguments into a dictionary
#           useful so that a function can accept a varrying amount of keyword arguments

def hello(**kwargs):
    print("Hello " + kwargs["first"] + " " + kwargs["last"])
    for key,value in kwargs.items():
        print(value, end=" ")

hello(first="Anh", last="phan")

#You can name **kwargs anything else as long as there is ** in front
#**kwargs is most common




