isHasCar = True
count = 0

while isHasCar and count != 3:
    count += 1
    if input("Enter pass: ") == "Stop":
        isHasCar = False
    elif count == 3:
        print("Try in another time")

