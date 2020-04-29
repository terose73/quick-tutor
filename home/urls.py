from django.urls import path, include
from django.contrib.auth import logout

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.login, name='login'),
    path('map/', views.map, name='map'),
    path('updateprofile/', views.updateProf, name='updateProfile'),
    path('submit_location/', views.submit_location, name='submit_location'),
    path('create_user/', views.create_user, name="create_user"),
    path('users_list/', views.users_list, name="users_list"),
    path('home/', views.home, name="home")
]
