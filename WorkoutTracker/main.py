import requests
import datetime as dt


APP_ID = "Your App id"
API_KEY = "Your Api Key"
API_ENDPOINT = "Your NutritionX Endpoint"
GENDER = "male"
WEIGHT = 0
HEIGHT = 0
AGE = 0
SHEETY_ENDPOINT = (
    "Your sheety endpoint"
)
TOKEN = "Your Bearer Token"

# Exercise Input


def input_exercise():
    exercise_text = input("Tell me which exercise you did: ")
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }
    body = {
        "query": exercise_text,
        "gender": GENDER,
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": AGE,
    }
    response = requests.post(url=API_ENDPOINT, headers=headers, json=body)
    return response


# Retrieving exercise data and time


def retrieve_exercise_data_and_time():
    today = dt.datetime.now()
    time_now = str(today.time()).split(".")[0]
    today_str = today.strftime("%d/%m/%Y")
    print(today_str)
    response = input_exercise()
    exercises = response.json()["exercises"]
    workouts = [
        {
            "date": today_str,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
        for exercise in exercises
    ]

    return workouts


# Posting to Google Sheets


def post_to_sheets(workouts):
    headers = {
        "Authorization": TOKEN
    }

    for workout in workouts:
        body = {
            "workout": workout
        }
        response = requests.post(
            url=SHEETY_ENDPOINT, json=body, headers=headers)
        print(response.json())


workouts = retrieve_exercise_data_and_time()
post_to_sheets(workouts=workouts)
