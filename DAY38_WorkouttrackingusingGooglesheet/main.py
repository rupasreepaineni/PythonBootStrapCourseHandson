import requests
from datetime import datetime

API_KEY = "nix_live_crtEnowWVmPFzX0oXyyxBzAjNLw8Kb15"
API_ID = "app_23f2dfaf10334bb3a137a636"

natural_exercise_endpt = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint = "https://api.sheety.co/pysuclearning/My_Workouts/workouts"
Query = input("Enter what exercise you did?")
exercise_params = {
    "query" : Query ,#"ran 3 miles and cycled for 20 minutes",
  # "weight_kg": input("Enter your weight in kg"),                 # Optional: Weight in kg (1-500)
  # "height_cm": input("Enter your height in cm"),                 # Optional: Height in cm (1-300)
  # "age": input("Enter your age"),                        # Optional: Age (1-150)
  # "gender": input("Enter your gender")
}
headers = {
    "x-app-id" : API_ID,
"x-app-key": API_KEY,
}
response = requests.post(url = natural_exercise_endpt , json = exercise_params, headers = headers)
print(response.status_code)
print(response.text)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
data = response.json()
for exercise in data["exercises"]:
    sheet_inputs= {
        "workouts" :{
        "date" : today_date,
        "time" : now_time,
        "exercise" :  exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
    }
    }
sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

print(sheet_response.text)