
# Tip Calculator program


print ("Welcome to the Tip Calculator")
bill = float(input("Enter the total bill\n"))
no_of_people = int(input("Enter the no. of people\n"))
tip = int(input("Enter the percentage of tip you would like to give\n"))
bill_plus_tip = (tip/100)*bill + bill
contribution_by_each = bill_plus_tip / no_of_people
print(f"The bill is {bill} and the total bill with tip is {bill_plus_tip}. As there are {no_of_people} people so each one's contribution will be {round(contribution_by_each, 2)}")