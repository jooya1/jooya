from django import forms
from django.contrib.auth.models import User

from  .models import Things

class ThingsForm(forms.ModelForm):

    class Meta:
        model = Things
        fields = ['title', 'description', 'image']
