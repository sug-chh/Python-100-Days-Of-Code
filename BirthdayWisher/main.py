##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "Your Email"
PASS_WORD = "Your Password"

# 1. Update the birthdays.csv


# 2. Check if today matches a birthday in the birthdays.csv
def random_letter_generator():
    letter_no = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_no}.txt") as letter_data:
        random_letter = letter_data.read()
        ready_to_send_letter = random_letter.replace("[NAME]", birthday_name)
    return ready_to_send_letter


# Function to compose the mail


def compose_mail(ready_to_send_letter):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASS_WORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_email,
            msg=f"Subject:Happy Birthday\n\n{ready_to_send_letter}",
        )


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

data = pandas.read_csv("birthdays.csv")

data_dict = {(row["day"], row["month"]): row for (key, row) in data.iterrows()}

now = dt.datetime.now()
date_tuple = (now.day, now.month)

if date_tuple in data_dict:
    birthday_name = data_dict[date_tuple]["name"]
    birthday_email = data_dict[date_tuple]["email"]
    composed_email = random_letter_generator()
    compose_mail(ready_to_send_letter=composed_email)
    print("Email sent successfully!!!")
else:
    print("It seems no one has his birthday today!!!")

# Function to generate a random letter
