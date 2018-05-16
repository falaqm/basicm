import urllib.request
import xml.etree.ElementTree as ET

sample='http://python-data.dr-chuck.net/comments_42.xml'
actual='http://python-data.dr-chuck.net/comments_217218.xml'
f=urllib.request.urlopen(actual).read()

tree=ET.fromstring(f)

counts=tree.findall('.//count')
total=0

for c in counts:
    total+=int(c.text)

print('total',total)

