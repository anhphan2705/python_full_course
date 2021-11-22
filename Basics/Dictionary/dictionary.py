#Dictionary =   A changable, unordered collection of unique key:value pairs
#               Dictionary is fast because it uses hashing, allow us to access a value quickly

capital = {"USA":"Washington D.C", 
            "India":"New Dehli",
            "Vietnam":"Hanoi",
            "Russia":"Moscow"}

#dict[key] = value : add a new key or overwrite old key
capital["Korea"] = "Seoul"
print(capital)

#dict[key] = Return value associated with the key
print(capital["Russia"])        

#dict.get(key) = Get the value associated with the key. Safer way to get a value from the dictionary
print(capital.get("Germany"))  

#dict.keys() = return all the keys
print(capital.keys())

#dict.values() = return all the value
print(capital.values())

#dict.items() = return every items in the dictionary
print(capital.items())

for key,value in capital.items():
    print(key, value)

#dict.update({key:value}) = add/update a item into the dictionary
capital.update({"Germany":"Berlin"})
capital.update({"USA":"Banana"})

#dict.pop(key)) = remove a a pair contains key in the dictionary
capital.pop("China")

#dict.clear() = clear all items in the dictionary
capital.clear()