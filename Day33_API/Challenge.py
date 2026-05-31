#if the ISS is close to my current position then send me an email to tell me to look up and see the ISS
import requests
from datetime import datetime
import smtplib
import time

my_lat = 55.771745
my_lng = -4.236272

my_email = "pysuclearning@gmail.com"
password = "godn airl elwg znuj"

parameters = {
    "lat" : my_lat,
    "lng" : my_lng,
    "formatted": 0, # this will give the time in ISO format which is easier to work with in python,
    # if we set it to 1 then it will give the time in
    # 12 hour format with AM and PM which is not so easy to work with in python
}

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)
    iss_longtitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    #your location is within +5 or -5 degrees of the ISS position
    if (my_lat-5 <= iss_latitude <= my_lat+5) and (my_lng-5 <= iss_longtitude <= my_lng+5):
        return True

def is_night():
    night_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    night_response.raise_for_status()
    data_night = night_response.json()
    sunrise =int(data_night['results']['sunrise'].split("T")[1].split(":")[0]) # this will give us the hour of sunrise time
    sunset = int(data_night['results']['sunset'].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
while True:
     time.sleep(60) # this will make the program to check every 60 seconds
     if is_iss_overhead() and is_night():
         with smtplib.SMTP("smtp.gmail.com") as connection:
             connection.starttls()
             connection.login(user=my_email, password=password)
             connection.sendmail(my_email,
                                 "my_email", "Subject:Look Up👆\n\nThe ISS is above you in the sky.")
