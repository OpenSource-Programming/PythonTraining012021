num = 0
tot = 0
print('\n🔢 🧑‍💻  Enter only numerical characters and type "done" when complete. ✅\n')
while True : 
	enterNum = input('Enter a number ➡️  ')
	if enterNum == 'done' :
		print('\n✅')
		break
	try:
		numEntry = float(enterNum)
	except:
		print('❌ Invalid entry.')
		continue
	num = num + 1
	tot = tot + numEntry
	mean = tot/num

print("\n🧮  Total of all entered numbers: " + str(tot))
print("💯  Amount of separate numerical entries: " + str(num))
print("💥  Average of all entries: " + str(mean) + "\n\n🎉 YAY‼️")
