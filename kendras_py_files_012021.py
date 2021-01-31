# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
add = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    #print(line)
    #atpos = line.find('0')
    #print(atpos)
    host = float(line[19:])
    #print(count)
    #print(host)
    add = add + host
print('Average spam confidence:', add/count)
