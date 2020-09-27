from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from django.core.paginator import Paginator

import requests, json, datetime

from todolist.models import Todolist

# Create your views here.

Year, Month, Day = 2020, 9, 3
# URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key=uqqKQ6Nn9R8jAN5gFJlObX2DU4r90z8d'
URL = 'https://api.nytimes.com/svc/archive/v1/2020/9.json?api-key=uqqKQ6Nn9R8jAN5gFJlObX2DU4r90z8d'

with open('sample.json', 'r') as openfile:
    json_object = json.load(openfile)

def news_home(request):
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

    return render(request, 'newspapers/home.html', {'articles': page_obj, 'events_id': events_id, 'today': datetime.datetime.now()})
