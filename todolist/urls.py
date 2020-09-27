from django.urls import path
from .views import TodolistCreateView, TodolistUpdateView, TodolistDeleteView #, TodolistListView
from . import views

urlpatterns = [
    # path('todolist/', TodolistListView.as_view(), name='todolist-home'),
    path('todolist/', views.todolist_home, name='todolist-home'),
    path('todolist/new/', TodolistCreateView.as_view(), name='event-create'),
    path('todolist/<int:pk>/update', TodolistUpdateView.as_view(), name='event-update'),
    path('todolist/<int:pk>/delete', TodolistDeleteView.as_view(), name='event-delete'),
]

