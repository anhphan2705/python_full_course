#tuple =    collection which is ordered and unchangable
#           used to group together related data

student = ("Anh", 18, "male")

for info in student:
    print(info)

#tuple.count(value) = count how many time a value appears
print(student.count("Anh"))

#tuple.index(value) = find the index of the value
print(student.index("male"))

