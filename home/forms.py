from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import*


class UpdateUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username',)


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['status', 'subject']

