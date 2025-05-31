def func():
    yield 1
    yield 2
    yield 3

for i in func():
    print(i)
    # Without for loop we get only single num