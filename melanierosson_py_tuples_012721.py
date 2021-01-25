# playing with colors in my terminal
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


filename = input('\n✨ Enter File: ' + bcolors.OKCYAN)
if len(filename) < 1 : filename = 'words.txt'
fullfile = open(filename)

# creates dictionary out of file contents (unsorted)
dictionary = dict()

for line in fullfile : 
	line = line.rstrip()
	words = line.split()
	for w in words:
		dictionary[w] = dictionary.get(w,0) + 1

# tuples list of key value pairs
tempList = list()
for k,v in dictionary.items() :
    newTuples = (v,k)
    tempList.append(newTuples)

#sort list
tempList = sorted(tempList, reverse=True)

print(bcolors.HEADER + '\n5' + bcolors.WARNING + ' most common words\nsorted in ' + bcolors.HEADER + 'descending' + bcolors.WARNING + ' order\ncontent is from ' + bcolors.OKCYAN + filename.upper() + bcolors.WARNING + ':\n' + bcolors.ENDC )
for v,k in tempList[:5] :
    print(bcolors.HEADER + str(k) + bcolors.WARNING + ' | ' + bcolors.OKCYAN + str(v) + bcolors.ENDC)
print('\n🥳\n')
