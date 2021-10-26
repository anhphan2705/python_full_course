#Not truly random. It's sudo random

import random

#random.randint(start, stop) = generate a random number from start (inclusive) to stop (exclusive)
print(random.randint(1, 6))

#random.randint() = generate a random float from 0 to exclusive 1
print(random.randint())

#random.choice(list) = generate a random choice from the list of value
my_list = ["rock", "paper", "scissors", 1, 2, 3]
print(random.choice(my_list))

#random.shuffle(list) = randomly shuffle a list
random.shuffle(my_list)
print(my_list)