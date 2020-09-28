from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from django.core.paginator import Paginator

from .models import Todolist
from .forms import TodolistForm

import datetime

# Create your views here.

# class TodolistListView(ListView):
#     model = Todolist
#     template_name = 'todolist/todolist_home.html'
#     context_object_name = 'events'
#     # ordering = ['-start_time']
#     paginate_by = 5

#     def get_queryset(self):
#         filter_val = self.request.user.id
#         order = self.request.GET.get('orderby', 'start_time')
#         new_context = Todolist.objects.filter(author_id=filter_val).order_by(order)
#         return new_context

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['events_id'] = Todolist.objects.filter(author_id=self.request.user.id).order_by("start_time")
#         context['today'] = datetime.datetime.now()
#         return context

def todolist_home(request):
    events_id = Todolist.objects.filter(author_id=request.user.id).order_by("start_time")

    paginator = Paginator(events_id, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todolist/todolist_home.html', {'events': page_obj, 'events_id': events_id, 'today': datetime.datetime.now()})


class TodolistCreateView(LoginRequiredMixin, CreateView):
    model = Todolist
    form_class = TodolistForm
    template_name = 'todolist/todolist_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['events_id'] = Todolist.objects.filter(author_id=self.request.user.id).order_by("start_time")
        context['today'] = datetime.datetime.now()
        return context

class TodolistUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todolist
    form_class = TodolistForm
    template_name = 'todolist/todolist_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        return  self.request.user == event.author

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['events_id'] = Todolist.objects.filter(author_id=self.request.user.id).order_by("start_time")
        context['today'] = datetime.datetime.now()
        return context

class TodolistDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todolist
    success_url = '/todolist/'

    def test_func(self):
        event = self.get_object()
        return  self.request.user == event.author

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['events_id'] = Todolist.objects.filter(author_id=self.request.user.id).order_by("start_time")
        context['today'] = datetime.datetime.now()
        return context