
#for a day and three hours both are same, we can use cnt parameter to get weather
# forecast for 4 times which is 3 hours apart so it will give us weather forecast for 12 hours


# 55.842073,-4.280899
# api.openweathermap.org/data/2.5/forecast?lat=55.842073&lon=-4.280899&appid=05bfa4040b723bb3cf95852d9f8fe8ef

import requests

LAT = 55.842073
LON = -4.280899
api_key = "05bfa4040b723bb3cf95852d9f8fe8ef"

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

# for hour_data in weather_data["list"]:
#     # print(hour_data['weather'][0]['id'])
#     weather_condition = hour_data['weather'][0]['id']
#     if weather_condition <= 700:
#         print("It'll rain in the next 12 hours, don't forget to take an umbrella ☔")

#                    OR--------------

will_rain = False
for hour_data in weather_data["list"]:
    # print(hour_data['weather'][0]['id'])
    weather_condition = hour_data['weather'][0]['id']
    if weather_condition <= 700:
        will_rain = True
if will_rain:
    print("It'll rain in the next 12 hours, don't forget to take an umbrella ☔")