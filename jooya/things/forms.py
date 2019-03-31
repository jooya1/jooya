from django import forms
from  .models import Things


class ThingsForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Things
        fields = ['title', 'description', 'image']
