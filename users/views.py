from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from todolist.models import Todolist

import datetime

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('news-home')
    else:
        form = UserRegisterForm()

    events_id = Todolist.objects.filter(author_id=request.user.id).order_by("start_time")

    return render(request, 'users/register.html', {'form': form, 'events_id': events_id, 'today': datetime.datetime.now()})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        print('testetes', user_form, profile_form)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    events_id = Todolist.objects.filter(author_id=request.user.id).order_by("start_time")
    
    content = {
        'user_form': user_form,
        'profile_form': profile_form,
        'events_id': events_id,
        'today': datetime.datetime.now()
    }
    return render(request, 'users/profile.html', content)