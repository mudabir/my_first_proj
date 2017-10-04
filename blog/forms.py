from django import forms
# from blogs.models import Blogs
from blogs.models import UserProfile
from django.contrib.auth.models import User
class BlogForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class UsersForm(forms.ModelForm):


# def __init__(self,*args,**kwargs):
#     super(BlogForm,self).__init__(*args,**kwargs)
#     self.fields['FirstName'].required = True
#     self.fields['LastName'].required = True
#     self.fields['UserName'].required = True
#     self.fields['Email'].required = True



    class Meta:
        model =  UserProfile
        fields = ['user','phone_number','address']

    # def __init__(self,*args,**kwargs):
    #     super(User,self).__init__(*args,**kwargs)
    #     self.fields['user'].required = True
    #     self.fields['PhoneNumber'].required = True
    #     self.fields['Address'].required = True
    #
    # class Meta:
    #     model = User
    #     fields = ['user','PhoneNumber','Address']