#Logical Statement (and, or, not) = used to if two or more conditional statement are true
temp = int(input("Please enter the temperature outside: "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today")
elif temp < 0 or temp > 30:
    print("Stay in, weather sucks")
