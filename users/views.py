from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from records.models import *
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрированы!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required(login_url='users/login/')
def profile(request):
    therapist = None
    selected_feelings = None
    selected_methods = None
    selected_events = None
    if request.user.user_type == 'TH':
        therapist = Therapist.objects.get(user=request.user)
        selected_feelings = therapist.feelings.values_list('name', flat=True)
        selected_methods = therapist.methods.values_list('name', flat=True)
        selected_events = therapist.events.values_list('name', flat=True)
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'form': form, 'methods': Methods.objects.all(),
        'selected_feelings': selected_feelings,
        'selected_methods': selected_methods,
        'selected_events': selected_events ,
        'feelings': Feelings.objects.all(),
        'events': Events.objects.all(),
        'therapist': therapist,
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:login'))
