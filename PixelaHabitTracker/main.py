import requests
from datetime import datetime

TOKEN = "Your Token "
USERNAME = "Your Username"
GRAPH_ID = "Your GRAPH_ID"


choice = input("Create/ Update/ Delete a Pixel ? : ").lower()

pixela_endpoint = "https://pixe.la/v1/users"

headers = {"X-USER-TOKEN": TOKEN}


# Functions:
# Create a pixel
def create_pixel(date):
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_data = {
        "date": date.strftime("%Y%m%d"),
        "quantity": input("How many kilometers did you cycle today?: "),
    }
    response = requests.post(
        url=pixel_creation_endpoint, json=pixel_data, headers=headers
    )
    print(response.text)


# Update a Pixel
def update_pixel(date):
    update_endpoint = (
        f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"
    )
    new_pixel_data = {
        "quantity": input("Please enter the value you wanna update the pixel with : ")
    }
    response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
    print(response.text)


# Delete a pixel
def delete_pixel(date):
    delete_endpoint = (
        f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"
    )
    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)



if choice == "update" or choice == "delete":
    year = int(input("Enter the year : "))
    month = int(input("Enter the month : "))
    day = int(input("Enter the day : "))
    today = datetime(year=year, month=month, day=day)
    if choice == "update":
        update_pixel(date=today)
    else:
        delete_pixel(date=today)

elif choice == "create":
    today = datetime.now()
    create_pixel(date=today)

else:
    print("Please provide a valid input!")
