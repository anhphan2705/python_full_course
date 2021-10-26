#Exception = events detected during execution that interrupt the flow of a program

#try = test to see if there is any error in this block of code
try:
    numerator = int(input("Enter a number to divide: "))
    denomerator = int(input("Enter a number to divide by: "))
    result = numerator / denomerator
#except = catch the declared error
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by 0")
except ValueError as e:
    print(e)
    print("Only number is accepted")
except Exception as e:
    print(e)
    print("Something went wrong :(")
#else = if there is no error detected, run the code inside
else: 
    print(result)
#finally = run the code inside no matter what happen above
finally: 
    print("This will always execute")
