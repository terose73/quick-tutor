from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.context_processors import auth
from home.models import UserProfile


def logout_view(request, next_page):
    user = auth(request)['user']

    # sets a user to "offline" once they have logged out
    user.userprofile.online = False
    user.userprofile.save()

    logout(request)
    return HttpResponseRedirect(redirect_to=next_page)
