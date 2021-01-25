# Exercise 10.2

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count_hr_dict = {}
for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] == "From":
        hr = words[5].split(":")[0]
        count_hr_dict[hr] = count_hr_dict.get(hr, 0) + 1

sorted_hrs_lst = sorted([(k,v) for k, v in count_hr_dict.items()])
for hr, count in sorted_hrs_lst:
    print(hr, count)