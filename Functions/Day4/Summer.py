def summer(arr):
    total=0
    skip=False
    for i in arr:
        if i==6:
            skip=True
        elif i==9 and skip:
            skip=False
        elif not skip:
            total=total+i
    return total

print(summer([4,5,6,7,8,9]))