from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Things(models.Model):
    description = models.CharField(max_length=4000)
    date_added = models.DateField(auto_now=True)
    user = models.ForeignKey(User, related_name='things')
    #image = models.ImageField()
    
    
