



# Highest score checker

student_score = input("Enter the score obtained by the students\n")
student_score = student_score.split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
high_score = max(student_score)
print(f"The high score is {high_score}")

# Highest score checker writing code manually

student_scores = input("Enter the score obtained by the students\n")
student_scores = student_scores.split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

heighest_score = 0
for score in student_scores:
    if score > heighest_score:
        heighest_score = score
print(f"The highest score in the class is: {heighest_score}")

# For in range loop
sum = 0
for i in range(0, 101):
    if i % 2 == 0:
        sum = sum + i
print(sum)