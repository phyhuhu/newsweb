from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import requests, json, datetime, os

from todolist.models import Todolist
from .models import Forecast

# get the key for new York Times from secret.py
from .secret import KEY_NYT

def news_home(request, **kwargs):

    # get today's Year, Month, Day
    time_now=datetime.datetime.now()
    Year, Month, Day = time_now.year, time_now.month, time_now.day

    # requests articles from NYT for Year Month
    URL = f'https://api.nytimes.com/svc/archive/v1/{Year}/{Month}.json?api-key={KEY_NYT}'
    nytimes = requests.get(URL)
    articles = json.loads(nytimes.text)['response']['docs']

    new_articles=[]

    for i in range(len(articles)):
        article=articles[i]
        titledata = article['headline']['main']
        datedata = article['pub_date']
        
        # change the datetime format
        if isinstance(datedata, str):
            temp = datedata[:10]+' '+datedata[11:19]+'.'+datedata[20:]
            datedata = datetime.datetime.strptime(temp, '%Y-%m-%d %H:%M:%S.%f')
            articles[i]['pub_date'] = datedata

        # select today's articles
        if articles[i]['pub_date'].day == Day:
            new_articles.append(articles[i])

    # setup paginatorto show 10 articles per page
    paginator = Paginator(new_articles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # get todolist from database
    events_id = Todolist.objects.filter(author_id=request.user.id).order_by("start_time")

    # get weather information from database
    latest_forecast = Forecast.objects.get(city='Houston')

    content = {
        'articles': page_obj,
        'events_id': events_id,
        'today': datetime.datetime.now(),
        'weather': {
            'main': latest_forecast.main,
            'description': latest_forecast.description,
            'temperatue': latest_forecast.temperatue,
            'wind': latest_forecast.wind,
            'time': latest_forecast.timestamp
            }
        }

    return render(request, 'newspapers/home.html', content)
