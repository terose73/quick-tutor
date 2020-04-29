from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    online = models.BooleanField(default=False)
    latitude = models.DecimalField(
        max_digits=10, decimal_places=7, default=0.0000000)
    longitude = models.DecimalField(
        max_digits=10, decimal_places=7, default=0.0000000)
    status = models.CharField(max_length=15, default='Hanging Out')
    subject = models.CharField(max_length=150, default='School Work')
    geodata = models.CharField(max_length=50)

    def __str__(self):
        return F"Username: {self.user.email} is Online: {self.online}"

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        else:
            instance.userprofile.save()