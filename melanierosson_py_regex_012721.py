# taste the rainbow
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# importing re????
import re

# opening file
filename = 'regex_sum_1136998.txt'
filetxt = open(filename)

# creates dictionary out of file contents (unsorted)
dictionary = dict()

for line in filetxt : 
	line = line.rstrip()
	words = line.split()
	for w in words:
		dictionary[w] = dictionary.get(w,0) + 1

# turns dictionary into strings
stringFile = str(dictionary)

regex = '[0-9]+'
sumInts = 0  
countInts = 0

# finds all integers in the file
integers = re.findall(regex, stringFile)

# counts and finds sum of integers
for eachInt in integers :
	eachInt = eachInt.rstrip()

	countInts = countInts + 1
	sumInts = sumInts + int(eachInt)

print(bcolors.WARNING + '\n💣  The ' + bcolors.HEADER + 'total number' + bcolors.WARNING + ' of integers in ' + bcolors.OKCYAN + filename + bcolors.WARNING + ' is ' + bcolors.OKGREEN + str(countInts) + bcolors.WARNING)
print('💥  The ' + bcolors.HEADER + 'sum '  + bcolors.WARNING + 'of all the integers in ' + bcolors.OKCYAN + filename + bcolors.WARNING + ' is ' + bcolors.OKGREEN + str(sumInts) + bcolors.ENDC + '\n')
