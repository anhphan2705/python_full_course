#function = a block of code which is executed only when it is called

def hello():
    print("Hellow world")
hello()

def print_name(first_name, last_name, age):
    print("Hello " + first_name + last_name)
    print("You are currently " + str(age) + " years old")
print_name("Anh", "Phan", 18)