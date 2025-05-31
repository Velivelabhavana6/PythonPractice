from collections import Counter
a=[1,32,43,1,3,34,89,234,4,1,32,32,23,4,32]
c=Counter(a)
# print(c)
# Its also count the string
# Most common return the highest to lowest
# For Eg
top=c.most_common(2)
print(top)
# in  the place of arg 2 means, gives highest 2 num
