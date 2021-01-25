hrs = input("Enter Hours: ")
h = float(hrs)
rte = input("Enter Rate Per Hour: ")
r = float(rte)
stanpay = h * r
times = r * 0.5
ot = (h - 40.0) * (times)
finover = stanpay + ot

if h > 40 :
    print(finover)
else:
    print(stanpay)
