#str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"
number = 3.14159

print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item))                         #positional argument
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))    #keyword argument 

text = "The {} jumped over the {}"
print(text.format(animal, item))

#{left_space:right_space}
print("Hello my name is {:10}. Nice to meet you.".format(item))    #add 10 space to the right

#{:<num_space} = align the text to the left in the num_space
print("Hello my name is {:<10}. Nice to meet you.".format(item)) 

#{:>num_space} = align the text to the right in the num_space
print("Hello my name is {:>10}. Nice to meet you.".format(item)) 

#{:^num_space} = align the text to the middle in the num_space
print("Hello my name is {:^10}. Nice to meet you.".format(item)) 

#{:.(digit)f} = display the float with certain number of digit after the .
print("The number of pi is {:.2f}".format(number))

#{:,} = add a comma for every thousandth 
print("The magic number is {:,}".format(69696969))

#{:b} = display the input number as binary numebr
print("The number is {:b}".format(69))

#{:o} = display the input number as octa number
print("The number is {:o}".format(69))

#{:X} = display the input number as hexadecimal
print("The number is {:X}".format(69))

#{:e} (lowercase) or {:E} (uppercase) = display the input number in scientific number 
print("The number is {:e}".format(69))
print("The number is {:E}".format(69))