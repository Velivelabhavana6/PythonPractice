# def even_num(num):
#     res = num%2 == 0
#     print(res)

# even_num(4)

# Checking list of even
# def check_even_list(number):
#     for i in number:
#         if i %2 == 0:
#             print(i)
#         else:
#             pass
        
# check_even_list([3,32,4])

#Adding in to list to even
def even_list(num):
    evenNumbers=[]
    for i in num:
        if(i%2==0):
            evenNumbers.append(i)
        else:
            pass
    return evenNumbers
        
print(even_list([2,34,6,5]))
