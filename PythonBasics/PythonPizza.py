# Python Pizza A Longer Way


# bill = 0
# peporani_bill = 0
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, L\n")
# add_pepperoni = input("Do you want pepperoni? Y or N\n")
# extra_cheese = input("Do you want extra cheese? Y or N\n")

# if size == "L":
#     print("Large Pizza : $25")
#     bill = 25
#     if add_pepperoni == "Y":
#         bill += 3
#         if extra_cheese == "Y":
#             bill += 1
#         else:
#             bill = bill
#     else:
#         if extra_cheese == "Y":
#             bill += 1
#         else:
#             bill = bill
# elif size == "M":
#     print("Medium pizza : $20")
#     bill = 20
#     if add_pepperoni == "Y":
#         bill += 3
#         if extra_cheese == "Y":
#             bill += 1
#         else:
#             bill = bill
#     else:
#         if extra_cheese == "Y":
#             bill += 1
#         else:
#             bill = bill
# else:
#     print("Small pizza: $15")
#     bill = 15
#     if add_pepperoni == "Y":
#         bill += 3
#         if extra_cheese == "Y":
#             bill += 1
#         else:
#             bill = bill
#     else:
#         if extra_cheese == "Y":
#             bill += 1
#         else:
#             bill = bill
# print(f"Your total bill is : {bill}")


# Python Pizza in a shorter method


bill = 0
peporani_bill = 0
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")


if size == "L":
    print("Large pizza $25")
    bill += 25
elif size == "M":
    print("Medium size: $20")
    bill += 20
elif size == "S":
    print("Small pizza: $15")
    bill += 15
else:
    print("Please enter a valid input")

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
else:
    bill = bill
if extra_cheese == "Y":
    bill += 1
else:
    bill = bill
print(f"Your final bill is ${bill}")
