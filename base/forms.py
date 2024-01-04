from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

#Create user (Model Form)
class CreateUserForm(UserCreationForm):
    
    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
#Authentication user (Model Form)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)