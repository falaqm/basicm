import urllib.request  
from bs4 import BeautifulSoup  
url = input('Enter URL ')  
count = input('Enter count: ')  
count = int(count)  
pos = input('Enter position: ')  
pos = int(pos)-1  
html = urllib.request.urlopen(url).read()  
seq = ''  
for i in range(0,count):
    soup = BeautifulSoup(html,'html.parser')  
    tags = soup('a')  
    seq = seq + tags[pos].contents[0]+' '  
    html = urllib.request.urlopen(tags[pos].get('href', None)).read()  
print("Sequence of names- ", seq ) 
print('Last name in sequence -', tags[pos].contents[0]) 
