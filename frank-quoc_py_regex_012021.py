import re

filename = "regex_sum_1131739.txt"
count = 0
with open(filename) as fn:
    for line in fn:
        line = line.rstrip()
        nums = list(map(float, re.findall('[0-9]+', line)))
        if len(nums) == 0:
            continue
        else:
            count += sum(nums)
print(int(count))


