largest = 0
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        innum = int(num)
    except: 
        print("Invalid input")
        continue    
    if smallest is None:
    	smallest = innum
    elif innum < smallest:
        smallest = innum
    elif innum > smallest:
    	largest = innum
    	if innum > largest:
            largest = innum
        
       
print("Maximum is", largest)
print("Minimum is", smallest)
