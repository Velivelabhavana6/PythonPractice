#fibonacci series
def fibo(nums):
    x,y=0,1
    for n in range(nums):
        x,y=y,x+y
        yield x
for x in fibo():
    print(x)
fibo(10)
    

        