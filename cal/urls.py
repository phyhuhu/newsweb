from django.urls import path
# from django.conf.urls import url
from .views import CalendarView
from . import views

app_name = 'cal'
urlpatterns = [
    path('cal/', views.event, name='cal-home'),

    # url(r'^index/$', views.index, name='index'),
    # url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    # url(r'^event/new/$', views.event, name='event_new'),
	# url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]

