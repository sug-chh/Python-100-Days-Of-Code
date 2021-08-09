# Python treasure map

print("Welcome to Python Treasure Map")
row1 = ["@", "@", "@"]
row2 = ["@", "@", "@"]
row3 = ["@", "@", "@"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?\n")
horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

map[vertical][horizontal] = "X"


print(f"{row1}\n{row2}\n{row3}")
