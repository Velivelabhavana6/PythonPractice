from collections import defaultdict
# d={'a':10}
# print(d['a'])
d=defaultdict(lambda: 20)
d['correct']=100
print(d['correct'])
# If i give wrong key bydefault it assigned lambda value
print(d['wrong'])