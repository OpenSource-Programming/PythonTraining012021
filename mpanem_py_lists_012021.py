txtfile = open('mbox-short.txt')

for line in txtfile :
	# stripping whitespace from the entire file
	line = line.rstrip()
	# splitting lines into lists
	firstword = line.split()
	# gaurdian in a compound statement
	# skipping lines that begin with:
		# words that have less than 3 letters
			# OR
		# whose words DO NOT start with 'From'
	if len(firstword) < 3 or firstword[0] != 'From' :
		continue
	# printing the third word each remaining line list
	# (which is always the 3-letter day of the week)
	print(firstword[2])
