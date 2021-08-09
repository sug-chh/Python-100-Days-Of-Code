import random
import math

random_interger = random.randint(100, 200)
print(random_interger)

random_float = math.floor((random.random()) * 100)
print(random_float)
love_score = random.randint(0, 100)
print(f"Your love score is {love_score}")


print("Flip a Coin")
coin = math.floor(random.random() * 2)
if coin == 0:
    print("Heads!")
else:
    print("Tails!")