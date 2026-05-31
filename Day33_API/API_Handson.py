import requests

# API endpoint URL
response = requests.get("http://api.open-notify.org/iss-now.json")
print(response)
#we can raise the exceptions whatever we wanted to handle
#response.raise_for_status()
data = response.json()
print(data)
longtitude = data['iss_position']
ts = data['timestamp']
print(ts)
print(longtitude)
long = data['iss_position']['longitude']
print(long)