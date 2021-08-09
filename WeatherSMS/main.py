import requests
from twilio.rest import Client
import smtplib

MY_LAT = 0
MY_LONG = 0
MY_EMAIL = ""
PASS_WORD = ""
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": "Your App Id",
    "units": "metric",
    "exclude": "daily,minutely,current",
}


#Compose Email
def compose_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASS_WORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="",
                msg=f"Subject:Alert\nIt's not gonna rain today. No need to carry your umbrella!",
            )


# send message

def send_message():
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="It's going to rain today.Remember to bring an ☔",
                        from_='',
                        to=''
                    )

    print(message.status)


response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall", params=parameters
)

response.raise_for_status()

weatherly_data = response.json()

hourly_data_for_12_hours = weatherly_data["hourly"][:12]




condition_codes_for_12_hours = []
will_rain = False


for hour_data in hourly_data_for_12_hours:
    condition_code = hour_data["weather"][0]["id"]
    condition_codes_for_12_hours.append(condition_code)
    if condition_code < 700:
        will_rain = True
print(f"Rain status: {will_rain}")


if will_rain == True:
    send_message()
else:
    compose_mail()

