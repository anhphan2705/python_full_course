#If statement = a block of code that will execute if its conditio is true

age = int(input("How old are you? "))

if age >= 18:
    print("Adult")
if age == 100:
    print("1 century old")
elif 0 < age < 18:
    print('Child')
else:
    print("Despawn")
