import requests

parameters = {"amount": 20, "type": "boolean"}

response = requests.get("https://opentdb.com/api.php", params=parameters)

data = response.json()
response.raise_for_status()

question_data = data["results"]

