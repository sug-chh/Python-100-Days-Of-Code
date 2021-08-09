# Rock Paper & Scissors

import random

print("Welcome to python Rock Paper Scissors")

user_chosen_no = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors!\n")
)
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


game = [rock, paper, scissors]

if user_chosen_no >= 3 or user_chosen_no < 0:
    print("You have chosen a wrong input so you loose!")
else:
    print(f"You chose:\n{game[user_chosen_no]}")

    computer = random.randint(0, 2)

    print(f"Computer chose:{(game[computer])}")

    if user_chosen_no == computer:
        print("Its is a draw")
    elif (
        (user_chosen_no == 0 and computer == 1)
        or (user_chosen_no == 1 and computer == 2)
        or (user_chosen_no == 2 and computer == 0)
    ):
        print("You lose")
    elif (
        (user_chosen_no == 0 and computer == 2)
        or (user_chosen_no == 1 and computer == 0)
        or (user_chosen_no == 2 and computer == 1)
    ):
        print("You Win")
