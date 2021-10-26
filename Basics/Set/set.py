#set = collection which is unordered, unindexed. No duplicate values
utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

for silverware in utensils:
    print(silverware)

#set.add(value) = add a value to a set
utensils.add("napkin")

#set.remove(value) = remove a value from a set
utensils.remove("fork")

#set.clear() = clear all value in a set
utensils.cealr()

#set.update(new_set) = add all value of a new set into the current set
utensils.update(dishes)

#set1.union(set2) = create a completely new set that contains the 2 sets
dinner_table = utensils.union(dishes)

#set1.diffence(set2) = return what set 1 has that set 2 doesn't
print(dishes.difference(utensils))
print(utensils.difference(dishes))

#set1.intersection(set2) = return teh common value between the sets
print(dishes.intersection(utensils))

