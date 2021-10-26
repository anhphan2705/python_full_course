#Loop Control Statement = change a looop execution from its normal sequence

#break = used to terminate the loop entirely
while True:
    name = input("Enter your name: ")
    if (name != ""):
        break
print()

#continue = skips to the next iteration of the loop
phone_number = "123-312-2454"
for char in phone_number:
    if char == "-":
        continue
    print(char, end="")
print()

#pass = does nothing, acts as a placeholder
for num in range(1, 21):
    if (num == 13):
        pass
    else:
        print(num, end=" ")