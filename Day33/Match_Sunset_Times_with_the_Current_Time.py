import requests
from datetime import datetime

My_lat = 51.507351
My_lng = -0.127758

prameters = {
    "lat": My_lat,
    "lng": My_lng,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=prameters)

response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunrise)

print(sunset)

print(time_now.hour)