
# Love Calculator


name1 = input("Enter the name of the first person\n")
name2 = input("Enter the name of the second peron\n")
name1 = name1.lower()
name2 = name2.lower()
t = name1.count("t") + name2.count("t")
print(f"T occurs {t} times")
r = name1.count("r") + name2.count("r")
print(f"R ocurrs {r} times")
u = name1.count("u") + name2.count("u")
print(f"U occurs {u} times")
e = name1.count("e") + name2.count("e")
print(f"E occurs {e} times")
true = (t + r + u + e)
print(f"Total = {true}")

l = name1.count("l") + name2.count("l")
print(f"L occurs {l} times")
o = name1.count("o") + name2.count("o")
print(f"O occurs {o} times")
v = name1.count("v") + name2.count("v")
print(f"V occurs {v} times")
e = name1.count("e") + name2.count("e")
print(f"E occurs {e} times")
love = (l + o + v + e)
print(f"Total = {love}")

true = str(true)
love = str(love)
love_score = true + love

if love_score <= "10" or love_score >= "90":
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= "40" and love_score <= "50":
    print(f"Your love score is {love_score}, you are alright together")
else:
    print(f"Your love score is {love_score}")