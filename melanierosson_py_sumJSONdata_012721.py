import json
import urllib.request

# download raw json object
url = "http://py4e-data.dr-chuck.net/comments_1137003.json"

# declare variables
sum = 0
count = 0

# ask user for JSON data URL
dataLocate = input('\n Enter URL to retrieve data: ')
# if no entry, use default URL from above
if len(dataLocate) < 1 : dataLocate = url

# grabbing JSON data from URL page
data = urllib.request.urlopen(dataLocate).read().decode()

# print URL pulling from
print('⭐', dataLocate)

# print characters in data
print('Retrieved', len(data), 'characters')

# function to search for JSON key and grab its value
def find_values(id, json_repr):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict

    json.loads(json_repr, object_hook=_decode_dict)
    return results

# using above function to create a for loop
# iterate through each instance of the count key
# + add instance to the total counter + add key value to the sum total
for eachCount in find_values('count', data) :
    count += 1
    sum += eachCount

# print counter
print(" Count:", count)
# print sum
print(" Sum:", sum, '\n')
