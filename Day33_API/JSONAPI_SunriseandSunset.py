#getting sunset and sunrise times for a specific location using the sunrise-sunset API

import requests

my_lat = 55.771745
my_lng = -4.236272

parameters = {
    "lat" : my_lat,
    "lng" : my_lng,
    "formatted": 0, # this will give the time in ISO format which is easier to work with in python,
    # if we set it to 1 then it will give the time in
    # 12 hour format with AM and PM which is not so easy to work with in python
}

response = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise)
print(sunrise.split("T")) #here T is the separator between date and time in ISO format
print(sunset)
print(f"Sunrise time is {sunrise} and Sunset time is {sunset}")