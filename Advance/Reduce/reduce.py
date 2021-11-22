# reduce() =    apply a function to an iterable and reduce it to a single cumulative value
#               performs function on first to elements and repeats process until 1 value remains
# Syntax: functools.reduce(function, iterable)

import functools

#Example 1
letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y: x + y, letters)

print(word)

#Example 2
factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)
# [5, 4, 3, 2, 1] => [20, 3, 2, 1] => [60, 2, 1] => [120, 1] => 120
print(result)