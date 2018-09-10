# from django.forms import forms
from django import forms

def _parsePhoneNumber(tel_number):
    return tel_number\
        .replace('(', '')\
        .replace(')', '')\
        .replace('_', '')\
        .replace('-', '')\
        .replace(' ', '')\
        .replace('+','')

class CustomSignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='Имя')
    last_name = forms.CharField(max_length=30, label='Фамилия')
    phone = forms.CharField(max_length=30, label='Телефон')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = _parsePhoneNumber(self.cleaned_data['phone'])

        user.save()