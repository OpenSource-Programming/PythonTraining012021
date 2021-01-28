import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    # Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
    # Actual data: http://py4e-data.dr-chuck.net/comments_1131743.xml (Sum ends with 89)
    count_sum = 0

    url = input('Enter location: ')
    if len(url) < 1: break
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode() # changes to UTF-8
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')   
    print('Count:', len(counts))
    for count in counts:
        count = int(count.text)
        count_sum += count
    
 
    print('Sum:', count_sum)
