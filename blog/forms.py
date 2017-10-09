from django import forms
# from blogs.models import Blogs
from blogs.models import UserProfile, ProductPurchase,ExampleModel
from django.contrib.auth.models import User



class BlogForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email','password']

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


# class RegistartionForm(forms.ModelForm):
#         class Meta:
#             model = UserRegistration
#             fields = ['first_name', 'last_name', 'username', 'email','password']
