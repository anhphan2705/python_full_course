# list comprehension = a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read

#Normal way
squares = []
for i in range(1, 11):
    squares.append(i * i)
print = squares

# list = [expression for item in iterable]
squares = [i * i for i in range(1, 11)]
print(squares)

# list = [expression for item in iterable if conditional]
students = [100, 90, 80, 70, 60, 50, 40 , 30, 0]
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

# list = [expression for item in iterable if conditional]
passed_students = [i for item in students if i >= 60]

# list = [expression (if/else) for item in iterable if conditional]
passed_students = [i if i >= 60 else "Failed" for item in students]

