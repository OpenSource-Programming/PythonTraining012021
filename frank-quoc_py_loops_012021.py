# Exercise 5.1
# num = 0 
# tot = 0.0
# while True:
#     sval = input("Enter a number: "")
#     if sval == "done":
#         break
#     try:
#         fval = float(sval)
#     except ValueError:
#         print("Invalid input")
#         continue
#     else:
#         num += 1
#         tot += fval
# print(tot, num, tot/num)

# Exercise 5.2
largest = float("-inf")
smallest = float("inf")
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try: 
        num = int(num)
    except: 
        print("Invalid input")
        continue
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
print("Maxumum is", largest)
print("Minimum is", smallest)