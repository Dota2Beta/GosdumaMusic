from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Application, User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'full_name', 'phone', 'email', 'password1', 'password2')
        labels = {
            'username': 'Логин',
            'full_name': 'ФИО',
            'phone': 'Телефон',
            'email': 'E-mail',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('title', 'event_date', 'genre', 'participation_format')
        labels = {
            'title': 'Название проекта/мероприятия',
            'event_date': 'Желаемая дата',
            'genre': 'Жанр музыки',
            'participation_format': 'Формат участия',
        }
        widgets = {'event_date': forms.DateInput(attrs={'type': 'date'})}


class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('status',)
