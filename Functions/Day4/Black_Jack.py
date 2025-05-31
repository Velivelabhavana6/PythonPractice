def black_jack(a,b,c):
    sum=a+b+c
    if sum<=21:
        return sum
    elif 11 in [a,b,c] and sum>=21:
        return sum-10
    elif sum>=21:
        return 'BUST'
    
print(black_jack(9,9,9))