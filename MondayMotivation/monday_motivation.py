import smtplib
import datetime as dt
import random

my_email = "Your Email"
pass_word = "Your Password"

with open("quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()
    random_quote = random.choice(quotes)

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)

if weekday == 4:  # Checking if weekday is friday

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pass_word)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg=f"Subject:Weekly Quotes\n\n{random_quote}",
        )
