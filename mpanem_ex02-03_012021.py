# calculate total pay for the hours worked
# rounds money to only 2 decimal places

hours = input("⏰ Enter Hours: ")
rate = input("💵 Enter Rate: ")
total = float(hours) * float(rate)
print("🤑 Pay: $" + str(round(total,2)))
