from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Things(models.Model):

    name = models.CharField(max_length=40)
    description = models.CharField(max_length=4000)
    date_added = models.DateField(auto_now=True)
    user = models.ForeignKey(User, related_name='things')
    image = models.ImageField(upload_to='things_pic', blank=True)

    def type_to_string(self):
        """Convert the type field to its string representation
        (the boneheaded way).
        """
        if self.type == 1:
            return "Sedan"
        elif self.type == 2:
            return "Truck"
        else:
            return "SUV"

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.name