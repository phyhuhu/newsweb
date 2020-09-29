import requests, json
from newspapers.models import Forecast
from django.contrib.auth.models import User
from datetime import datetime 

def _get_forecast_json():

    # URL = 

    # r = requests.get(URL)

    with open('weather.txt') as json_file:
        r = json.load(json_file)
    try:
        # r.raise_for_status()
        return r #r.json()
    except:
        return None


def update_forecast():
    json = _get_forecast_json()

    if json is not None:
        try:
            # open weather map gives temps in Kelvin. We want celsius.
            temp_in_celsius = str(float("{:.2f}".format(json['main']['temp'] * 1.8 - 459.67)))
            wind_in_celsius = str(float("{:.2f}".format(json['wind']['speed'] *3600 / 1609.344)))

            if len(Forecast.objects.filter(city='Houston'))!=0:

                Forecast.objects.filter(city='Houston').update(timestamp=datetime.now())
                Forecast.objects.filter(city='Houston').update(temperatue=temp_in_celsius)
                Forecast.objects.filter(city='Houston').update(wind=wind_in_celsius)
                Forecast.objects.filter(city='Houston').update(description=json['weather'][0]['main'])
                Forecast.objects.filter(city='Houston').update(description=json['weather'][0]['description'])
                Forecast.objects.filter(city='Houston').update(city=json['name'])

            else:
                
                new_forecast = Forecast(
                    main = json['weather'][0]['main'],
                    description = json['weather'][0]['description'],
                    temperatue = temp_in_celsius,
                    wind = wind_in_celsius,
                    city = json['name']
                    )
                new_forecast.save()

        except:
            pass
