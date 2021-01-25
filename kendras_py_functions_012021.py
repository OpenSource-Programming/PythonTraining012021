def computepay(hours, rate) :
    if hours > 40 :
        stanpay = hours * rate
        times = rate * 0.5
        ot = (hours - 40.0) * (times)
        pay = stanpay + ot
    else:
        pay = hours * rate
    return pay
        

hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter Rate: ")
r = float(rte)

xp = computepay(h,r)
print('Pay', xp)
