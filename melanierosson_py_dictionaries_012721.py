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

# I changed his confusing variable acronyms
filename = input('Enter File: ')
if len(filename) < 1 : filename = 'words.txt'
fullfile = open(filename)

dictionary = dict()

for line in fullfile : 
	line = line.rstrip()
	words = line.split()
	for w in words:
		dictionary[w] = dictionary.get(w,0) + 1
print(bcolors.WARNING + '\n📖 dictionary of ' + bcolors.OKCYAN + filename.upper() + bcolors.ENDC)
print(dictionary,'\n')

# find most common word
numtimes = -1
mostword = ""

print(bcolors.WARNING + '\n💬 word count of ' + bcolors.OKCYAN + filename.upper() + bcolors.ENDC)

for k,v in dictionary.items() :
	print(k,v)
	if v > numtimes :
		numtimes = v
		mostword = k

print(bcolors.OKGREEN + '\nDONE ✅' + bcolors.WARNING)
print('most frequent word in ' + bcolors.OKCYAN + filename.upper() + bcolors.WARNING + ' is ', bcolors.HEADER + str(mostword), bcolors.WARNING + ' which appears ', bcolors.HEADER + str(numtimes), bcolors.WARNING + ' times.')
