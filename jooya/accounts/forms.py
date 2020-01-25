from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = 'حداکثر ۱۵۰ کاراکتر - تنها شامل حروف و اعداد انگلیسی باشد.'
        self.fields['password1'].help_text = '<li>پسورد شما نباید شبیه اطلاعات شخصی شما باشد.</li>' \
                                             '<li>پسورد شما باید حداقل شامل ۸ کاراکتر باشد.</li>' \
                                             '<li>پسورد شما نباید از پسورد‌های رایج باشد.</li>' \
                                             '<li>پسورد شما نباید فقط شامل اعداد باشد.</li>'
        self.fields['password2'].help_text = 'پسورد خود را دوباره وارد نمایید.'
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
