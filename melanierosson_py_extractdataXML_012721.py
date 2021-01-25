import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

sum = 0

dataLocate = input('\n Enter URL to retrieve data: ')
if len(dataLocate) < 1 : dataLocate = 'http://py4e-data.dr-chuck.net/comments_42.xml'

pageData = urllib.request.urlopen(dataLocate)
data = pageData.read()

print('⭐', dataLocate)
print('\n Characters:', len(data))

tree = ET.fromstring(data)
counts = tree.findall('.//count')

for count in tree.iter('count'):
    strNum = count.text
    intNum = int(strNum)
    sum += intNum

print(" Count:", len(counts))

print(" Sum:", sum, '\n')
