# FizzBuzz in Python in Python Lists

print("Welcome to Fizzbuzz Python With Lists")
num = []
for n in range(0, 101):
    num.insert(n, n)
    # print(num)
    if n != 0:
        if n % 3 == 0:
            num.insert(n, "FIZZ")
        # print(num)
        if n % 5 == 0:
            num.insert(n, "BUZZ")
        # print(num)
        if n % 3 == 0 and n % 5 == 0:
            num.insert(n, "FIZZBUZZ")
        # print(num)
    else:
        n = 0
print(num)




# FizzBuzz in Python Loop

print("Welcome to Fizzbuzz Python with Loops")
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0 :
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")

    else:
        print(n)
