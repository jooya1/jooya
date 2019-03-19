from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Things(models.Model):
    title = models.CharField(max_length=1000, default='title')
    description = models.CharField(max_length=4000)
    date_added = models.DateField(auto_now=True)
    user = models.ForeignKey(User, related_name='things')
    image = models.ImageField(upload_to='things_pic', blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.title

