#index operator [] = gives access to a sequence's element (str, list, tuples)

name = "anh phan"

if (name[0].islower()):
    print(name.capitalize())

first_name = name[0:3].upper()
print(first_name)

last_name = name[4:].lower()
print(last_name)

last_char = name[-1]    #Using negative indexing



