"""Users Forms"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    """Users SignUp Form"""
    first_name = forms.CharField(max_length=50, help_text='Last Name')
    last_name = forms.CharField(max_length=50, help_text='Last Name')
    email = forms.EmailField(max_length=60, help_text='Email')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                'email', 'password1', 'password2',
                )

class ProfileUpdateForm(UserChangeForm):
    """Users Update Profile Form"""
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=60)
    username = forms.CharField(max_length=50)
    #last_login = forms.CharField(max_length=50)
    #is_superuser = forms.CharField(max_length=50)
    #is_staff = forms.CharField(max_length=50)
    #is_active = forms.CharField(max_length=50)
    #date_joined = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                'email', 'password'
                )

