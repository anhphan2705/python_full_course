# map() = applies a function to each item in an iterable (list, typles, etc.)
# Syntax: map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jackets", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1]*0.82)
to_dollars = lambda data: (data[0], data[1]/0.82)

# Apply the to_euros function to store 
store_euros = list(map(to_euros, store))
store_dollars = list(map(to_dollars, store))

for i in store_euros:
    print(i)

for i in store_dollars:
    print(i)