import re
text="the agent phone"
patt='phone'
# print(re.search(patt,text))
abc='My phone  numn is "789-000-0000'
# phone=re.search('7890000',abc)
# phone=re.search('\d\d\d\d\d\d\d',abc)
# print(phone.group())
#gives the num
# phone=re.search(r'\d{3}-\d{3}-\d{4}',abc)
# print(phone)
phone_patt=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
res=re.search(phone_patt,abc)
print(res.group(3))