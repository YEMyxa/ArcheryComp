from typing import Any
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Profile

User = get_user_model()


class UserCreationForm(UserCreationForm):
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя',
                                      'class':       'auth-forms-label'})
    )

    email = forms.EmailField(
        label=_('Email'),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email',
                                       'placeholder' : 'Email',
                                       'class':        'auth-forms-label'})
    )
    
    password1 = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'placeholder' : 'Пароль',
                                          'class':        'auth-forms-label'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'placeholder' : 'Подтвердите пароль',
                                          'class':        'auth-forms-label'}),
        strip=False,
        help_text=_('Подтвердите пароль для верификации.'),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {'username':'Имя пользователя',
                  'email':'Email',
                  'first_name':'Имя',
                  'last_name':'Фамилия'}
        


class ProfileUpdateForm(forms.ModelForm):
    
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'ГГГГ-ММ-ДД'}),
                                    required=False)
    date_of_birth.default_error_messages = {
        "invalid": _("Введите дату в форме: ГГГГ-ММ-ДД"),
    } 

    class Meta:
        model = Profile
        fields = ['second_name','sex',
                  'date_of_birth', 'rank',
                  'region','organization',
                  'coach']
        labels = {'second_name':'Отчество',
                  'sex':'Пол',
                  'date_of_birth':'Дата рождения', 
                  'rank':'Звание',
                  'region':'Регион',
                  'organization':'Организация',
                  'coach':'Тренер'}
        
        error_messages = {  #'second_name':'',
        #                     'sex':'',
                            'date_of_birth': {'invalid':_('Форма даты: ГГГГ-ММ-ДД'),
                                              'invalid_date':_('Форма даты: ГГГГ-ММ-ДД')}, 
                            # 'rank':'',
                            # 'region':'',
                            # 'organization':'',
                            # 'coach':''
                         }
        

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
                                attrs={'autofocus': True,
                                       'placeholder': 'Имя пользователя',
                                       'class':       'auth-forms-label'}))
    password = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                          'placeholder': 'Пароль',
                                          'class':       'auth-forms-label'}),
    )

    
