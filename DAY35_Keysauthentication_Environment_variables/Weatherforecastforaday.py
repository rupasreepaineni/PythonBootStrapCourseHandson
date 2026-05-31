# 55.842073,-4.280899
# api.openweathermap.org/data/2.5/forecast?lat=55.842073&lon=-4.280899&appid=05bfa4040b723bb3cf95852d9f8fe8ef

import requests

LAT = 55.842073
LON = -4.280899

PARAMS = {
    "appid": "05bfa4040b723bb3cf95852d9f8fe8ef",
    "lat": LAT,
    "lon": LON,
}



weather_response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params = PARAMS)
weather_response.raise_for_status()
print(weather_response.status_code)
weather_data = weather_response.json()
print(weather_data)
