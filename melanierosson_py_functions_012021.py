# function
def computepay(h, r) :
	print("\n🧮 Computepay function: " + str(h) + " hours / $" + "{:.2f}".format(r) + " hourly wage")
	if h > 40 :
		# overtime
		regpay = r * h
		overtime = (h - 40.0) * (r * 0.5)
		print("\nTotal Regular Pay")
		print("💲 $" + "{:.2f}".format(regpay))
		print("Total Overtime Pay")
		print("💲 $" + "{:.2f}".format(overtime))
		total = regpay + overtime
	else:
		#regular
		total = h * r
		print("\n✅ Regular Pay Only: $" + "{:.2f}".format(total))
	return total

# user prompts
hours = input("⏰ Enter Hours: ")
rate = input("💵 Enter Rate: $")

try:
	fh = float(hours)
	fr = float(rate)
except:
	print("⚠️  Error: please enter numeric values for all inputs.")
	quit()

total = computepay(fh,fr)
# identify whether this is only regular pay versus has overtime pay

# print total result
print("\n🤑 Total Overall Pay: 💲 $" + "{:.2f}".format(total) + " 💰")
