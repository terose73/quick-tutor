import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.context_processors import auth
from django.urls import reverse
from .models import UserProfile
from .forms import *
import os
from dotenv import load_dotenv


def map(request):
    user = auth(request)['user']
    if user.is_authenticated:


             # sets the user to be online when they are on the map
            user.userprofile.online = True
            user.userprofile.save()

            users_list = User.objects.all()

            non_admin_users_list = []

            # removes the admin from the list of online users  displayed
            for user in users_list:
                if not user.is_staff:
                    non_admin_users_list.append(user)

            # makes sure people are online in the context users list
            online_users = [
                person for person in non_admin_users_list if person.userprofile.online == True]

            return render(request, 'home/map.html', {'users_list': online_users})

    else:
        return HttpResponseRedirect(reverse('home:login'))


def create_user(request):
    user = auth(request)['user']
    if not hasattr(user, 'userprofile'):
        profile = UserProfile()
        profile.user = user
        profile.save()

    return HttpResponseRedirect(reverse('home:map'))


def submit_location(request):
    user = auth(request)['user']
    load_dotenv()
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

    if user.is_authenticated:
        if request.method == 'GET':
            return
        elif request.method == 'POST':
            d = request.POST.dict()
            user.userprofile.latitude = d['latitude']
            user.userprofile.longitude = d['longitude']
            user.userprofile.save()

            response = requests.get(
                F'https://maps.googleapis.com/maps/api/geocode/json?latlng={user.userprofile.latitude},{user.userprofile.longitude}&key={GOOGLE_API_KEY}')
            geodata = "".join(response.json(
            )['results'][0]['formatted_address'].split(',')[0:3])

            user.userprofile.geodata = geodata
            user.userprofile.save()
            return HttpResponse('')
    else:
        return render(request, 'home/login.html', {})


def login(request):
    user = auth(request)['user']
    if user.is_authenticated:
        return HttpResponseRedirect(reverse('home:map'))
    else:
        return HttpResponseRedirect(reverse('home:home'))


def home(request):
    return render(request, 'home/login.html', {})


def users_list(request):
    user = auth(request)['user']
    if user.is_authenticated:
        users_list = User.objects.all()

        non_admin_users_list = []

        # removes the admin from the list of online users  displayed
        for user in users_list:
            if not user.is_staff:
                non_admin_users_list.append(user)

        # makes sure people are online in the context users list
        online_users = [
            person for person in non_admin_users_list if person.userprofile.online == True]

        return render(request, 'home/users_list.html', {'users_list': online_users})
    else:
        return render(request, 'home/login.html', {})


def updateProf(request):

    user = auth(request)['user']
    if user.is_authenticated:
        if request.method == 'POST':
            user_form = UpdateUser(request.POST, instance=request.user)
            profile_form = UserProfileForm(
                request.POST, instance=request.user.userprofile)
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save(commit=False)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return HttpResponseRedirect(reverse('home:users_list'))

        else:
            profile_form = UserProfileForm(instance=request.user.userprofile)
            user_form = UpdateUser(instance=request.user)
            args = {'user_form': user_form, 'profile_form': profile_form}
            return render(request, 'home/updateprofile.html', args)

    else:
        return render(request, 'home/login.html', {})
