import requests

import datetime as dt
import smtplib
import time

MY_LAT = 0
MY_LONG = 0
MY_EMAIL = "Your Email"
PASS_WORD = "Your Password"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# Sunrise & sunset tracker

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])

sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(f"Sunrise: {sunrise}, Sunset: {sunset}")


# Look at the sky email:
def look_at_the_sky():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASS_WORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="To address",
            msg=f"Subject:Iss Nearby\n\nHey there the Iss is nearby look at the sky!!!\nCurrent Latitude:{iss_position['lat']},Current Longitude:{iss_position['lng']}",
        )


# Iss tracker
def iss_tracker():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    iss_position = {"lat": latitude, "lng": longitude}
    return iss_position


is_tracking_on = True


while is_tracking_on:
    iss_position = iss_tracker()
    print(f"\n{iss_position}")
    now = dt.datetime.utcnow()
    current_time = now.hour
    print(f"Current hour: {current_time}")

    if current_time >= sunset or current_time <= sunrise:
        print("It's already dark")

        if (
            iss_position["lat"] <= (MY_LAT + 5.00)
            and iss_position["lat"] >= (MY_LAT - 5.00)
            and iss_position["lng"] <= (MY_LONG + 5.00)
            and iss_position["lng"] >= (MY_LONG - 5.00)
        ):
            look_at_the_sky()
            print("The Iss is nearby! Please look up.")
        else:
            print("Iss is quite far away!!!")

    else:
        print("It's not dark yet")
        
    
    
    time.sleep(60)


    


#Angela's way


# def is_iss_overhead():
#     response = requests.get(url="http://api.open-notify.org/iss-now.json")
#     response.raise_for_status()
#     data = response.json()

#     iss_latitude = float(data["iss_position"]["latitude"])
#     iss_longitude = float(data["iss_position"]["longitude"])

#     #Your position is within +5 or -5 degrees of the iss position.
#     if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
#         return True


# def is_night():
#     parameters = {
#         "lat": MY_LAT,
#         "lng": MY_LONG,
#         "formatted": 0,
#     }
#     response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
#     response.raise_for_status()
#     data = response.json()
#     sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
#     sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

#     time_now = dt.datetime.now().hour

#     if time_now >= sunset or time_now <= sunrise:
#         return True


# while True:
#     time.sleep(60)
#     if is_iss_overhead() and is_night():
#         connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
#         connection.starttls()
#         connection.login(MY_EMAIL, PASS_WORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_EMAIL,
#             msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
#         )

