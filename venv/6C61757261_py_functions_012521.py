def computepay(h, r):
    hour = float(h)
    rate = float(r)
    pay = 0.0
    if hour > 40.0:
        overtime = hour - 40.0
        pay = (overtime) * (rate * 1.5)
        hour -= overtime
        # print("overtime! ", hour, pay)
    pay += hour * rate

    return pay


hrs = input("Enter Hours:")
rt = input("Enter Rate: ")
p = computepay(hrs, rt)
print("Pay", p)