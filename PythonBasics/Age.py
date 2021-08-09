# Age Calculator program in Python

current_age = int(input("Enter your current age\n"))
age_remaining = 90-current_age
no_of_days_remaining = age_remaining*365
no_of_weeks_remaining = age_remaining*52
no_of_months_remaining = age_remaining*12

print(f"You have {no_of_days_remaining} days, {no_of_weeks_remaining} weeks, and {no_of_months_remaining} months left")