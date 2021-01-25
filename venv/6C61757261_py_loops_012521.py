largest = None
smallest = None
arr = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            arr.append(int(num))
        except:
            print("Invalid input")

# print(arr)

print("Maximum is", max(arr))
print("Minimum is", min(arr))