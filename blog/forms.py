from django import forms
# from blogs.models import Blogs
from blogs.models import UserProfile, ProductPurchase,ExampleModel
from django.contrib.auth.models import User



class BlogForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email','password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':'Enter Name'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter email'}),
            'password': forms.TextInput(attrs={'placeholder': 'Enter Password'})
        }


class UsersForm(forms.ModelForm):
    class Meta:
        model =  UserProfile
        fields = ['user','phone_number','address']


class ProductPurchaseForm(forms.ModelForm):
    class Meta:
        model = ProductPurchase
        fields = ['title','price']


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()


class loginForm(forms.Form):
    username = forms.CharField(error_messages={'required': 'Email is required'}, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email'}))
    password = forms.CharField(error_messages={'required':'Password is required'},widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))

