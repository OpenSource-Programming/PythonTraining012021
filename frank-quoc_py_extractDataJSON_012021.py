import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True: 
    # Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
    # Actual data: http://py4e-data.dr-chuck.net/comments_1131744.json (Sum ends with 65)
    sum_count = 0
    url = input("Enter location: ")
    if len(url) < 1: break
    
    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode() # changes to UTF -8
    print("Retrieved", len(data), "characters")
    info = json.loads(data)
    print('Count:', len(info["comments"]))
    # print(info)

    for comment in info["comments"]:
        sum_count += comment["count"]
    print(sum_count)