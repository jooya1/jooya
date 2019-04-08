from django.db import models

# Create your models here.
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    link = models.CharField(max_length=30, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            a = Account()
            a = Account.objects.create(user=instance)
            a.save()
