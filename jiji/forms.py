
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

from .models import Interests, Product


class SignUpForm(UserCreationForm): 
    first_name = forms.CharField(max_length=30, required=False, )
    last_name = forms.CharField(max_length=30, required=False, )
    #username = forms.CharField(max_length=30, required=False, widget=forms.HiddenInput)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email', 'state_of_residence', 'password1', 'password2',)
  


class LoginForm(forms.ModelForm):
    email = forms.EmailField(max_length=250)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields =('name','price','description','image',)

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interests
        fields =('name','email','location')
