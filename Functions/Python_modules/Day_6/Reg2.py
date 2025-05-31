import re
# res=re.search(r'caut','The cat is here')
# print(res)
# res1=re.findall(r'.at',"the cat in the hat and sat")
# print(res1)
# res2=re.findall(r'^\d',"2 is num")
# print(res2)

ph='there are! 3 num 34 5 this sen'
# pat=r'[^\d]+'
# print(re.findall(pat,ph))
#remove punctu
print(re.findall(r'[^!.?]+',ph))
