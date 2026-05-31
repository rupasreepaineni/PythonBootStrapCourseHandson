#sending SMS if it rains in the next 12 hours using openweathermap API and twilio API
#usageof environment variable
import requests
from twilio.rest import Client
import os

LAT = 55.842073
LON = -4.280899
api_key = "05bfa4040b723bb3cf95852d9f8fe8ef"
# account_sid = "ACe28f23f80605528b4d81d2e9237b42f2"
TWILIO_ACCOUNT_SID = "ACe28f23f80605528b4d81d2e9237b42f2"
auth_token = os.environ.get["auth_token"]
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")

PARAMS = {
          "lat": LAT,
          "lon": LON,
        "appid": api_key,
    "cnt" : 4 #this will give weather forecast for 4 times which is 3 hours apart so it will give us weather forecast for 12 hours
}

weather_response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params = PARAMS)
weather_response.raise_for_status()
print(weather_response.status_code)
weather_data = weather_response.json()
# print(weather_data["list"][0]['weather'][0]['id'])

will_rain = False
for hour_data in weather_data["list"]:
    # print(hour_data['weather'][0]['id'])
    weather_condition = hour_data['weather'][0]['id']
    if weather_condition <= 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It'll rain in the next 12 hours, don't forget to take an umbrella ☔",
        from_="+15017122661",
        to="+15558675310",
    )

    print(message.body)