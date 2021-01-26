# Request-Response Cycle
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

# Scraping HTML Data with BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url =  "http://py4e-data.dr-chuck.net/comments_1131741.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # scrapes the tags for numbers
    str_tag = str(tag)
    nums = list(map(float, re.findall('[0-9]+', str_tag)))
    if len(nums) == 0:
        continue
    else:
        count += sum(nums)
print(int(count))

# Following Links with Beautiful Code
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))
print('Retrieving:', url)

for _ in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[pos-1].get('href', None) # ind = pos - 1
    print('Retrieving:', url)
print(tags[pos-1].contents[0])