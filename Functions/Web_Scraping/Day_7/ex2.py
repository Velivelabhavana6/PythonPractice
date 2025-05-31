import requests
import bs4
res=requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup=bs4.BeautifulSoup(res.text,'lxml')
# print(soup.select('.mw-file-element'))
com=soup.select('.mw-file-element')[0]
# print(com['src'])
k=requests.get('https://upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/20px-Symbol_support_vote.svg.png')
p=requests.get('https://www.google.com/url?sa=i&url=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fpencils&psig=AOvVaw2meIbWF2kgPGvswe6X3W1F&ust=1747991107945000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLD4kMTcto0DFQAAAAAdAAAAABAE')
# print(k.content)
f=open('my_com_image.jpg','wb')
print(f.write(k.content))
f.close()
f=open('pencil.jpg','wb')
print(f.write(p.content))
f.close()

