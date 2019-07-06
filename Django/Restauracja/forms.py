import django.forms as forms
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Table




class RegisterUserForm(forms.Form):
    login = forms.CharField(max_length=50)
    password_1 = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100, validators=[EmailValidator()])

    def clean(self):
        cleaned_data = super().clean()
        if User.objects.filter(username=cleaned_data['login']).exists():
            raise forms.ValidationError('Login Zajęty')
        if cleaned_data['password_1'] != cleaned_data['password_2']:
            raise forms.ValidationError('Hasła nie są takie same')
        return cleaned_data

class LoginForm(forms.Form):
    login = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class TableReservationForm(ModelForm):
    class Meta:
        model = Table
        fields = ['table_size', 'time_reservation']
