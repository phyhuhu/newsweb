from django.contrib.auth.models import User

import requests, json, datetime

key = 'f177b7bdf6f28d01cff7dc0325f92c37'
URL = 'http://api.openweathermap.org/data/2.5/weather?q=Houston,us&appid=f177b7bdf6f28d01cff7dc0325f92c37'

res_weather = requests.get(URL)

weather = json.loads(res_weather.text)

print(weather)