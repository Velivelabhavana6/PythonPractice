l=[1,2,3]
l.append(4)
print(l)
print(l.count(0))
print(l.count(1))
x=[1,2,3]
#GIVING SUB LIST
x.append([4,5])
print(x)
x=[1,2,3]
#GIVING ENTIRE LIST
x.extend([4,5])
print(x)
print(l.index(2))
l.insert(2,'inserted')
print(l)
ele=l.pop()
print(ele)
print(l.pop(0))
print(l)
#remove deletes the first occurences
l.remove('inserted')
print(l)
l.reverse()
print(l)