import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
longi = response.json()["iss_position"]["longitude"]
lati  = data = response.json()["iss_position"]["latitude"]
data = (longi, lati)

print(data)