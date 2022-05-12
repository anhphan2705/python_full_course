# zip(*iterables) = aggregate elements from two or more iterable (lists, tupples, sets, etc.)
#                   creates a zip object with paired elements stored in uples for each elements with in zip object

username = ["Dude", "Bro", "Mister"]
password = ("p@ssword", "abc123", "guest")

#zip(iterable_1, iterable_2) = type is object zip
users = zip(username, password)
#the result will combine each element of the same index in each iterable together

