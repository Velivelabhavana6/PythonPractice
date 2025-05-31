def two_evens(a,b):
    if a%2==0 and b%2==0:
        if a<b:
          print(a)
        else:
            print(b)
    else:
        if a>b:
            print(a)
        else:
            print(b)
two_evens(7,5)