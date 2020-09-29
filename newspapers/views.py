from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from django.core.paginator import Paginator

import requests, json, datetime

from todolist.models import Todolist

from .models import Forecast

# Create your views here.

Year, Month, Day = 2020, 9, 3


with open('sample.json', 'r') as openfile:
    json_object = json.load(openfile)

def news_home(request, **kwargs):
    # nytimes = requests.get(URL)
    # articles = json.loads(nytimes.text)['response']['docs']

    # print(articles)

    new_articles=[]

    articles = json_object['response']['docs']
    for i in range(len(articles)):
        article=articles[i]
        titledata = article['headline']['main']
        datedata = article['pub_date']
        
        if isinstance(datedata, str):
            temp = datedata[:10]+' '+datedata[11:19]+'.'+datedata[20:]
            datedata = datetime.datetime.strptime(temp, '%Y-%m-%d %H:%M:%S.%f')
            articles[i]['pub_date'] = datedata

        if articles[i]['pub_date'].day == Day:
            new_articles.append(articles[i])

    paginator = Paginator(new_articles, 10) # Show 10 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    events_id = Todolist.objects.filter(author_id=request.user.id).order_by("start_time")

    # weather
    # res_weather = requests.get(URL_Weather)
    # weather = json.loads(res_weather.text)

    latest_forecast = Forecast.objects.get(city='Houston')

    content = {
        'articles': page_obj,
        'events_id': events_id,
        'today': datetime.datetime.now(),
        'weather': {
            'main': latest_forecast.main, #weather['weather'][0]['main'],
            'description': latest_forecast.description, #weather['weather'][0]['description'],
            'temperatue': latest_forecast.temperatue, #float("{:.2f}".format(float(weather['main']['temp']) * 1.8 - 459.67)),
            'wind': latest_forecast.wind, #float("{:.2f}".format(float(weather['wind']['speed'])*3600/1609.344)),
            'time': latest_forecast.timestamp
            }
        }

    return render(request, 'newspapers/home.html', content)
