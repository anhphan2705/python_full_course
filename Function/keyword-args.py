#keyword arguments = arguements preceded by an identifier when we pass them to a function
#                   The order of the arguements doesn't matter, unlike positional arguements
#                   Python knows the names of the arguements that our function receives

def print_name(first_name, last_name, age):
    print("Hello " + first_name + last_name)
    print("You are currently " + str(age) + " years old")
    
print_name(last_name="Phan", age=18, first_name="Anh")