# reading and editing files

# exact match to video
# fh = open('mbox-short.txt')

# for lx in fh:
# 	ly= lx.rstrip()
# 	print(ly.upper())

# my customizations 👇
file = open('mbox-short.txt')

for line_each in file:
	# removing whitespace
	line_nowhite = line_each.rstrip()

	# swapping the character cases in the file
	line_funcase = line_nowhite.swapcase()

	# adding emojis to specific lines based on what they start with
	if line_funcase.startswith('x-') :
		print("👹 " + line_funcase)
		continue
	elif line_funcase.startswith('tO:') :
		print("🍤 " + line_funcase)
		continue
	elif line_funcase.startswith('rECEIVED:') :
		print("📨 " + line_funcase)
		continue
	elif line_funcase.startswith('mODIFIED:') :
		print("📝 " + line_funcase)
		continue
	elif line_funcase.startswith('dATE:') :
		print("📅 " + line_funcase)
		continue
	elif line_funcase.startswith('fROM:') :
		print("🥝 " + line_funcase)
		continue
	elif line_funcase.startswith('aUTHOR:') :
		print("🙃 " + line_funcase)
		continue
	elif line_funcase.startswith('dETAILS:') :
		print("🧩 " + line_funcase)
		continue
	elif line_funcase.startswith('tHIS') :
		print("🎪 " + line_funcase)
		continue
	elif line_funcase.startswith('yOU') :
		print("🤟 " + line_funcase)
		continue
	print(line_funcase)
