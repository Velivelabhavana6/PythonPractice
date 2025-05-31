# Squaring of num using generator
def squares(n):
    for i in range(n):
        yield i**2
    
for  y in squares(10):
    print(y)
    
#Squaring of num

def squares(n):
    res=[]
    for i in range(n):
        res.append(i**2)
    return res
for y in squares(10):
    print(y)