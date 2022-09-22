from main.models import TuBlog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django import forms
from . models import Blog, TuBlog

class BlogCreate(forms.ModelForm):
   class Meta:
       model = Blog
       fields = ["name","author","description","body","image"]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Tengo mis dos formularios para creación de blogs y para creación de usuario 