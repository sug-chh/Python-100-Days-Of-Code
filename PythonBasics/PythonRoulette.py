# Python Roulette

import random

print("Welcome to python Roulette")
names = input("Give me everybody's names, playing the game separated by a comma\n")
names = names.split(", ")
print(names)
length = len(names) - 1
num = random.randint(0, length)
print(f"{names[num]} is going to buy the meal today!")


# Python Roulette 2

# import random
# print("Welcome to python Roulette")
# names = input("Give me everybody's names, playing the game\n")
# names = names.split(", ")
# print(names)
# person_who_will_play = random.choice(names)
# print(person_who_will_play+" is going to buy the meal today!")





# More on python Lists


fruits =['Strawberry','Mango','Pineapple','Kiwi',"Passion Fruit", 'Bananas','Peaches']
vegetables = ["Spinach", "Brinjal", "Carrots","Pumpkin","Tomatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

print(dirty_dozen[1][1])