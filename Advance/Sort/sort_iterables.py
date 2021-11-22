# sort() method = use with list only
# sorted() function = use with iterable
#Unless it is a list you cant use list.sort() method

students = ["Squidwards", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]
students_info = [("Squidward", "F", 60),
                 ("Sandy", "A", 33),
                 ("Patrick", "D", 36),
                 ("Spongebob", "B", 20),
                 ("Mr. Krabs", "C", 78)]

## List

# sort() = Sorting a list
students.sort()
for i in students:
    print(i)

# sort(reverse=True) = Reverse sorting a list
students.sort(reverse=True)
for i in students:
    print(i)
    
# sort(key=Function) = sort through a nested list with a certain key function
grade = lambda grades:grades[1] #Declare that it wants to be sorted in order of grade which is in index of 1
students_info.sort(key=grade, reverse=False)
for i in students_info:
    print(i)
    

## Not List

# Sorted(iterable, key, reverse) = sorting function. Key and reverse are optional
sorted_students = sorted(students)
for i in students:
    print(i)

sorted_students = sorted(students, reverse=True)
for i in students:
    print(i)
    
# sort(key=Function) = sort through a nested tuple with a certain key function
age = lambda ages:ages[2] #Declare that it wants to be sorted in order of age which is in index of 2
sorted_students_info = sorted(students, key=grade)
for i in students_info:
    print(i)


