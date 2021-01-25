# Exercise 4.6

def computepay(hours, rate):
    # print("In computepay", hours, rate)
    pay = hrs * rate
    if hours > 40:
        overtime = (hours - 40.0) * (0.5 * rate)
        pay += overtime
    # print("Returning", pay)
    return pay

if __name__ == '__main__':
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    p = computepay(hrs, rate)

    print("Pay", p)
