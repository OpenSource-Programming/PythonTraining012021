# calculate total pay for the hours worked

# user prompts
hours = input("⏰ Enter Hours: ")
rate = input("💵 Enter Rate: ")
# convert to decimals through float variables
fh = float(hours)
fr = float(rate)
# identify whether this is only regular pay versus has overtime pay
if fh > 40 :
	# overtime
	regpay = fr * fh
	overtime = (fh - 40.0) * (fr * 0.5)
	print("\nRegular Pay")
	print("💲 $" + str(round(regpay,2)))
	print("Overtime Pay")
	print("💲 $" + str(round(overtime,2)))
	total = regpay + overtime
else:
	#regular
	print("Regular Pay Only")
	total = fh * fr
# print total result
print("\n🤑 Total Pay: 💲 $" + str(round(total,2)) + " 💰")
