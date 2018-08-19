from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField()
    fio = forms.CharField()
    phone = forms.CharField()
