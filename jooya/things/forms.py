from django import forms
from  .models import Things


class ThingsForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ThingsForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True

    class Meta:
        model = Things
        fields = ['title', 'description', 'image']
