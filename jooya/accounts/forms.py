from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput(), label='ایمیل')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        labels = {
            "first_name": "نام",
            "last_name": "نام خانوادگی",
            "username": "نام کاربری",
            "password1": "پسورد",
            "password2": "تکرار پسورد"
        }


class UserInformationUpdateForm(forms.ModelForm):
        email = forms.EmailField(label='ایمیل')

        class Meta:
            model = User
            fields = ('first_name', 'last_name', 'email', )
            labels = {
                "first_name": "نام",
                "last_name": "نام خانوادگی"
            }
