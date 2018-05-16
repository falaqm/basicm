import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

'''fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

counts = dict()
for line in fhand:
    words = line.decode().split()
    print(line.decode().strip())
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
print(counts)'''


url=input("enter -")
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,"html.parser")

#Retrieve all anchor tags
tags=soup("a")
for tag in tags:
    print(tag.get('href',None))



