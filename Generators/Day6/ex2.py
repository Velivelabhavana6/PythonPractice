import random
# random.randint(1,67)

def randnum(low,high,n):
    for i in range(n):
        yield random.randint(low,high)

for y in randnum(1,10,12):
    print(y)