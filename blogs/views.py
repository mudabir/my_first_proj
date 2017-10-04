from django.shortcuts import render,HttpResponseRedirect
from django.template.loader import get_template
from django.views.generic.edit import View
from blogs.models import Blogs
from blog.forms import BlogForm
from django.contrib.auth.models import User
from blogs.models import UserProfile
# from blog.forms import UserProfile


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
        return render(request,'Blog_templates/Blog.html',{'users':users})

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

class UserProfileView(View):
    def get(self,request):
        def post(self, request):
            form = UserProfile(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                UserName = data['user_name']
                PhoneNumber = data['phone_number']
                Address= data['address']

                print "post"
                User.objects.create(
                    user_name=UserName,
                    phone_number=PhoneNumber,
                    address=Address,

                )

                return HttpResponseRedirect('/list/')

            return render(request, 'Blog_templates/Blog.html', {"form": form})
