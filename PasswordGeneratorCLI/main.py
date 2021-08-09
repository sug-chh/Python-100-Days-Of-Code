# Password Generator Project
import random

password = []

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


length_of_letters = len(letters)

for n in range(0, nr_letters):
    ran_pass_index = random.randint(0, length_of_letters - 1)
    password += letters[ran_pass_index]


length_of_numbers = len(numbers)

for n in range(0, nr_numbers):
    ran_pass_index = random.randint(0, length_of_numbers - 1)
    password += numbers[ran_pass_index]
    # print(f"{password}", end="")

length_of_symbols = len(symbols)

for n in range(0, nr_symbols):
    ran_pass_index = random.randint(0, length_of_symbols - 1)
    password += symbols[ran_pass_index]
random.shuffle(password)

password_str = ""

for char in password:
    password_str += char

print(f"Your password is : {password_str}\n", end="")
