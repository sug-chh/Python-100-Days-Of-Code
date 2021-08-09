

#  Example code


total_height = 0
avg_height = 0
student_heights = input("Enter the height of the students\n")
student_heights = student_heights.split()
length = len(student_heights)
for height in student_heights:
    height = int(height)
    total_height += height
print(f"The average height of the students is {round(total_height/length)}")

# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(number_of_students)
# print(f'The average height of the students using loop is {round(total_height/number_of_students)}')
