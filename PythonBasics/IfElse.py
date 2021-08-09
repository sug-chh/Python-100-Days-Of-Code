# If else in python

bill = 0
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm\n"))
age = int(input("Enter the age of the rider\n"))
if height >= 120:
    print("Can ride")
    if age >= 18:
        bill = 12
        print("Adult tickets are $12")
    elif age >= 12 and age <= 18:
        bill = 7
        print("Youth tickets is $7")
    else:
        bill = 5
        print("Child tickets price are $5")
    want_photo = input("Do you want a photo taken? Y or N.\n")
    if want_photo == "Y":
        bill += 3
    # print(f"Your total bill will be {bill}")
    else:
        bill = bill
    print(f"Your total bill is {bill}")
else:
    print("Cant ride")