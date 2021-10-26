#Nested Loop = The "inner loop" will finish all of tis iterations before finishing one iteration of the "outer loop"

row = int(input("How many rows? "))
column = int(input("How mnay column? "))
symbol = input("Enter a symbol: ")

for i in range(row):
    for i in range(column):
        print(symbol, end="")
    print()