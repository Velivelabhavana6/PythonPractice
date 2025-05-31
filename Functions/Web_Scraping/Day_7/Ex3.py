#to get 2 star rating
import requests
import bs4
# https://books.toscrape.com/catalogue/page-2.html
base_url="https://books.toscrape.com/catalogue/page-{}.html"
res=requests.get(base_url.format(1))
soup=bs4.BeautifulSoup(res.text,'lxml')
prod=soup.select(".product_pod")
ex=prod[0]
# print(ex)
# print(ex.select(".star-rating.Three"))
ex.select('a')[1]['title']
two_star_titles=[]
for n in range(1,51):
    scrap_url=base_url.format(n)
    res=requests.get(scrap_url)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    books=soup.select(".product_prod")
    
    for book in books:

        if len(book.select('star-rating.Two'))!=0:
            book_title=book.select('a')[1]['title']
            two_star_titles.append(book_title)
            
print(two_star_titles)