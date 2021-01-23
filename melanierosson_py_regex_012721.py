# importing re
import re

# opening file
filename = 'regex_sum_1136998.txt'
filetxt = open(filename)

# declarations
regex = '[0-9]+'
sumInts = 0  
countInts = 0
integers = []
newIntList = []
newIntItemStr = ''

# stripping whitespace and finding integers in each line of the file
for line in filetxt : 
	line = line.rstrip()
	integers.append(re.findall(regex, line))
    
# removing empty list items in the file line lists (lines that had no integers)
onlyInts = [listItems for listItems in integers if listItems]

# stringifying everything (there are currently list items within the larger list)
for eachItem in onlyInts :
    for insideEach in eachItem :
        newIntItemStr = newIntItemStr + ' ' + insideEach
    newIntList = newIntItemStr
    # splitting separate items into a single list based on spaces
    numList = newIntList.split()

# getting final numbers from final integer list
for numItems in numList :
    # list item count
    countInts += 1
    # list items sum
    sumInts += int(numItems)

print('The total integer count is ' +  str(countInts))
print('The sum of all integers is ' + str(sumInts))
