from django.shortcuts import render,HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic.edit import View
from blog.forms import BlogForm
from django.contrib.auth.models import User
from blogs.models import UserProfile
from blog.forms import User
from blog.forms import UsersForm


class createUserView(View):
    def get(self,request):
        form = BlogForm()
        return render(request,'Blog_templates/Add.html',{"form" : form})

    def post(self,request):
        form = BlogForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            FirstName = data['first_name']
            LastName = data['last_name']
            UserName = data['username']
            Email = data['email']
            print "post"
            User.objects.create(
                first_name = FirstName,
                last_name = LastName,
                username = UserName,
                email = Email
            )

            return HttpResponseRedirect('/list/')

        return render(request,'Blog_templates/Blog.html',{"form" : form})

class BlogView(View):
    def get(self,request):
        print "get"
        users = User.objects.all()
        profiles=UserProfile.objects.all()
        return render(request,'Blog_templates/Blog.html',{'users':users,"profiles":profiles})

    def post(self, request):
        # form =  BlogForm(request.POST)
        id = request.POST.get('user_info')
        print id
        User.objects.get(id=id).delete()
        return HttpResponseRedirect('/list')
        # def post(self, request):
        #     form = BlogForm(request.POST)
        #     print request.POST.get('user_info')
        #     User.objects.delete(users.id)
        #
        #     return HttpResponseRedirect('/list')
        # # return render(request,'Blog_templates/Blog.html',{'users':users} )

class DeleteView(View):
    def get(self,request, user_id):
        User.objects.get(id=user_id).delete()
        return HttpResponseRedirect('/list')


# class UserProfileView(View):
#     def get(self,request):
#         form = User()
#         return render(request, 'Blog_templates/User_Profile.html',{'users':users,"profiles":profiles})
#
#
#     def post(self,request):
#         form = UserProfile(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             UserName = data['user_name']
#             PhoneNumber = data['phone_number']
#             Address= data['address']
#
#             print "post"
#             User.objects.create(
#                 user_name=UserName,
#                 phone_number=PhoneNumber,
#                 address=Address,
#             )
#
#             return HttpResponseRedirect('/list/')
#         return render(request, 'Blog_templates/User_Profile.html', {"form": form})
class UserProfileView(View):
    def get(self,request):
        print "get"
        users = User.objects.all()
        profiles=UserProfile.objects.all()
        return render(request,'Blog_templates/User_Profile.html',{'users':users,"profiles":profiles})

    # def post(self, request):
    #     # form =  BlogForm(request.POST)
    #     id = request.POST.get('user_info')
    #     print id
    #     User.objects.get(id=id).delete()
    #     return HttpResponseRedirect('/list')

class CreateUser(View):
    def get(self,request):
        Users = UsersForm()
        return render(request,'Blog_templates/Create_Profile.html',{'Users':Users})

    def post(self,request):
        form = UsersForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User = data['user']
            PhoneNumber = data['phone_number']
            Address = data['address']
            print "post"
            UserProfile.objects.create(
                user = User,
                phone_number = PhoneNumber,
                address = Address,
            )

            return HttpResponseRedirect('/list/')
        return render(request,'Blog_templates/Create_Profile.html',{'Users':Users})
