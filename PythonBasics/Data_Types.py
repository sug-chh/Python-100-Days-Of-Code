# Converting one data type to another


num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")


# Retreiving the values from a string

a = input("Type a two digit no. ")

first_digit = int(a[0])
second_digit = int(a[1])

print(first_digit+second_digit)


score = 0
h = 1.8
isWinning = True

print(
    f"your score is {score}, your height is {h}, you are winning is {isWinning}")
