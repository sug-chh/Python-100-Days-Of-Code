

# Leap year function in Python


print("Welcome to the leap year checker\n")
year = int(input("Enter the year to be checked\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Its a leap year")
        else:
            print("It is not a leap year")

    else:
        print("It is a leap year")
else:
    print("The year is not a leap year")
