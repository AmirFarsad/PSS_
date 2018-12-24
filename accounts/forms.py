from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from accounts import models
from django.conf import settings

from django.core import validators 



    
    


class UserForm(UserCreationForm):
    '''
    password = forms.CharField(widget = forms.PasswordInput())
    password_confirm = forms.CharField(widget = forms.PasswordInput())

    terms = forms.BooleanField(
    error_messages={'required': 'You must accept the terms and conditions'},
    )

    def clean(value):
        all_clean_data = super().clean()
        n1 = all_clean_data['password']
        n2 = all_clean_data['password_confirm']
        if n1 != n2:
            raise forms.ValidationError("passwords don't match")
     '''

    terms = forms.BooleanField(
    error_messages={'required': 'You must accept terms and conditions'},
    )

    class Meta():
        model = models.UserModel
        fields = ('username','email','password1','password2','Firstname','Lastname','Birth')
        widgets = {
            'Birth':forms.TextInput(attrs={'class':'datepicker'}),
            }


class ChangePasswordForm(forms.Form):
    confirmation_code = forms.CharField(max_length = 200)
    new_password = forms.CharField(widget = forms.PasswordInput())
    new_password_confirm = forms.CharField(widget = forms.PasswordInput())

    def clean(value):
        all_clean_data = super().clean()
        n1 = all_clean_data['new_password']
        n2 = all_clean_data['new_password_confirm']
        if n1 != n2:
            raise forms.ValidationError("passwords don't match")


class ConfirmationCodeForm(forms.Form):
    username = forms.CharField()




