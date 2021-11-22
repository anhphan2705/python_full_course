a_dictionary = {"a": 1, "b": 2, "c": 3}

# Call max(iterable, key=dict.get) with the same dictionary as both iterable and dict to find the key paired with the max value.
max_key = max(a_dictionary, key=a_dictionary.get)
print(max_key)

#Call dict.values() to get a dict_values object containing the values of dict. Call max(iterable) with the previous result as iterable to get the max value of the dictionary.
all_values = a_dictionary.values()
max_value = max(all_values)
print(max_value)