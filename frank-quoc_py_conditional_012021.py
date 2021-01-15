# Exercise 3.1
hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = hrs * rate
if hrs > 40:
	overtime = (hrs - 40.0) * (0.5 * rate)
	pay += overtime
print(pay)

# Exercise 3.2
# try:
#     hrs = float(input("Enter Hours: "))
#     rate = float(input("Enter Rate: "))
# except ValueError:
#     print("Error, please enter numeric input")
#     quit()
# else:
#     pay = hrs * rate
#     if hrs > 40:
#         overtime = (hrs - 40.0) * (0.5 * rate)
#         pay += overtime
#     print(pay)

# Exercise 3.3
try:
    score = float(input("Enter Score: "))
except ValueError:
    print("You have not input a valid number.")
    quit()
else:
    if (score > 1.0) or (score < 0.0):
    	print("Your score must be between 0 and 1 inclusive.")
    	quit()
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")