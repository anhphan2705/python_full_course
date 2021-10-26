import random
a = int(random.randint(0,1000000))
b = int(random.randint(0,1000000))
print(a)
print(b)
m = a%b
print(m)
while a >= b:
    a -= b
print(a)
print(b)
if m >a:
    print("more")
elif m == a:
    print("equal")
else:
    print("less")