# Excercise 9.4 

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

email_count = {}
for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] == "From":
        email_count[words[1]] = email_count.get(words[1], 0) + 1

max_count = 0
max_email = None
for email, count in email_count.items():
    if count > max_count:
        max_count = count
        max_email = email
print( max_email, max_count)