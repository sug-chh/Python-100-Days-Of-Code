# BMI Calculator program


mass = float(input("Enter your Mass in kgs\n"))
height = float(input("Enter your height in m\n"))
bmi = mass / (height ** 2)
print(f"Your bmi is  {round(bmi, 2)}")
if bmi <= 18.5:
    print("You my friend are underweight")
elif bmi > 18.5 and bmi < 25.0:
    print("You my friend are underweight")
elif bmi > 25 and bmi < 30:
    print("You my friend are overweight")
elif bmi > 30 and bmi < 35:
    print("You my friend are obese")
else:
    print("You my friend are clinically obese")