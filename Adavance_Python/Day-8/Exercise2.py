import requests
import bs4
base_url = "https://quotes.toscrape.com/"
res = requests.get(base_url)
soup=bs4.BeautifulSoup(res.text,'lxml')
soup.select('.author')
#AUTHORS
authors=set()
for name in soup.select(".author"):
    authors.add(name.text)
# print(authors)
# UNIQUE AUTHORS OF 10 PAGES
url="https://quotes.toscrape.com/"
authors=set()
for page in range(1,10):
    page_url=url+str(page)
    res=requests.get(page_url)
    soup=bs4.BeautifulSoup(res.text,"lxml")
    for name in soup.select('.author'):
        authors.add(name.text)
    
print(authors)
# CREATING QUOTES
i=[]
for i in soup.select('.text'):
    i.append(i.text)
    
# print(i)
# TOP 10 TAGS

# for tag in soup.select('.tag-item'):
#     print(tag.text)