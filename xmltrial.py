import xml.etree.ElementTree as ET

data= '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>
'''
tree=ET.fromstring(data)
print("Name:",tree.find('name').text)
print("Attr:",tree.find('email').get('hide'))

inpt= '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''
print('*'*50)
stuff=ET.fromstring(inpt)
lst=stuff.findall('users/user')
print('Count',len(lst))

for item in lst:
    print('Name',item.find('name').text)
    print('ID',item.find('id').text)
    print('Attribute',item.get('x'))
    
    
