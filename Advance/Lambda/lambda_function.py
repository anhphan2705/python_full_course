# Lambda function = function written in 1 line using labda keyword
#                   accepts any number of arguments, but only has one expression
#                   (think of it as a shortcut of function)
#                   (use full if needed for a short period of time, )
# Syntax: function_name = lambda parameters:expression

#Normal
def double(x):
    return x*2

print(double(5))

#Lambda function
double_lambda = lambda x : x*2
print(double_lambda(5))

multiply = lambda x,y : x*y
print(multiply(5,6))

add = lambda x,y,z : x+y+z
print(add(1, 2, 3))

full_name = lambda first_name, last_name : (first_name + " " + last_name)
print("Anh", "Phan")

age_check = lambda age : True if age >= 18 else False
print(age_check(18))