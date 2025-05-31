import requests
import bs4
res=requests.get("https://en.wikipedia.org/wiki/Virat_Kohli")
# print(type(res))
# print(res.text)

soup=bs4.BeautifulSoup(res.text,"lxml")
#  print(soup.select('p'))
# print(soup.select('title'))
# select will give info of headings like p,h1,text...abs
# print(soup.select('title')[0].getText())
# IT WILL NOT GIVE IN format of list
# site_para=soup.select("title")
# print(site_para[0].getText())
print(soup.select('.vector-dropdown-content'))