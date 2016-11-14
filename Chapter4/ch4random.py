# ch4random.py

import random

for i in range(10):
    x = random.random()
    print(x)


# randint
#  \n = new line
print("\n")
print("now we'll use randint")

for i in range(10):
    x = random.randint(1, 100)
    print(x)


# choice
print("\n")
print("using choice of {a,b,c,d,e,f,g}")

t = ['a','b','c','d','e','f','g']
for i in range(10):
    x = random.choice(t)
    print(x)