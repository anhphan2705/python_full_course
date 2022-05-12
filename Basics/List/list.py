#list = used to store multiple items in a single varible

food_list = ["pizza", "hamburger", "hotdog", "spaghetti"]
print(food_list[0]) 

for food in food_list:
    print(food)
    
#list.append(value) = add a new value to the list
food_list.append("ice cream")

#list.index(value) = find the index of the value in the list
food_list.index("ice cream")

#list.remove(value) = remove a value from the list
food_list.remove("hotdog")

#list.pop(index) = remove value at index. If no index is passed, the last value in the list will me removed 
food_list.pop()

#list.insert(index, value) = adding a value to the list at an index
food_list.insert(0, "fries")

#list.sort() = sort the list into alphabetical order
food_list.sort()

#list.clear() = clear all value in the list
food_list.clear()