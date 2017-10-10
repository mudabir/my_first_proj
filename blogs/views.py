from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.http import (HttpResponseForbidden)
from django.template.loader import get_template
from django.views.generic.edit import View
from blog.forms import BlogForm
from django.contrib.auth.models import User
from blogs.models import UserProfile
from blog.forms import User
from blog.forms import UsersForm
from blogs.models import ProductPurchase
from blog.forms import ProductPurchaseForm
from blog.forms import ImageUploadForm
from blogs.models import ExampleModel
from blog.forms import loginForm
# from blogs.models import UserRegistration
# from blog.forms import RegistartionForm


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


        # return render(request,'Blog_templates/Blog.html',{'users':users,"profiles":profiles})
        return render(request,'Blog_templates/index.html',{'users':users,"profiles":profiles})

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


class CreateProductView(View):
    def get(self,request):
        form = ProductPurchaseForm()
        return render(request,'Blog_templates/Create_Product.html',{"Products" : form})

    def post(self,request):
        form = ProductPurchaseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Title = data['title']
            Price = data['price']
            Price = data['price']
            ProductPurchase.objects.create(price=Price,title=Title)
            # print "post"
            # User.objects.create(
            #     title = Title,
            #
            # )

            return HttpResponseRedirect(reverse('productpurchaseURL'))
        return render(request,'/Blog_templates/Create_Product.html',{"Products" : form})

class ProductPurchaseView(View):
    def get(self, request):
        print "get"
        users = User.objects.all()
        Products = ProductPurchase.objects.all()
        print "Products", Products
        return render(request, 'Blog_templates/Product_Purchase.html', {"products": Products})


def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ExampleModel()
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')

class ProductsView(View):
    def get(self,request):
        print "get"
        users = User.objects.all()
        Products = ProductPurchase.objects.all()
        return render(request,'Blog_templates/Products.html',{"products": Products})

class UserRegisterationView(View):
    def get(self,request):
        form = BlogForm()
        return render(request,'Blog_templates/userregistration.html',{"form" : form})

    def post(self,request):
        form = BlogForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            FirstName = data['first_name']
            LastName = data['last_name']
            UserName = data['username']
            Email = data['email']
            Password=data['password']
            print "post"
            User.objects.create(
                first_name = FirstName,
                last_name = LastName,
                username = UserName,
                email = Email,
                password = Password
            )

            return HttpResponseRedirect('/Users_list/')

        return render(request,'Blog_templates/Users_list.html',{"form" : form})

class UsersView(View):
    def get(self,request):
        print "get"
        users = User.objects.all()
        profiles=UserProfile.objects.all()
        return render(request,'Blog_templates/Users_list.html',{'users':users,"profiles":profiles})


class LoginView(View):
    def get(self,request):
        form = loginForm()
        return render(request,'Blog_templates/login.html',{"form" : form})

    def post(self, request):
        form = loginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Email = data['email']
            Password = data['password']
            print "post"
            User.objects.create(
                email=Email,
                password=Password
            )

            return HttpResponseRedirect('/Users_list/')
        return render(request, 'Blog_templates/login.html', {"form": form})


class RegisterView(View):
    def get(self,request):
        form = BlogForm()
        return render(request,'Blog_templates/register.html',{"form" : form})

    def post(self, request):
        form = BlogForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            FirstName = data['first_name']
            LastName = data['last_name']
            UserName = data['username']
            Email = data['email']
            Password=data['password']
            print "post"
            User.objects.create(
                first_name=FirstName,
                last_name=LastName,
                username=UserName,
                email=Email,
                password=Password
            )

            return HttpResponseRedirect('/Users_list/')
        return render(request, 'Blog_templates/login.html', {"form": form})

class BlogView(View):
    def get(self, request):
            print "get"
            users = User.objects.all()
            profiles = UserProfile.objects.all()

            # return render(request,'Blog_templates/Blog.html',{'users':users,"profiles":profiles})
            return render(request, 'Blog_templates/index.html', {'users': users, "profiles": profiles})

    def post(self, request):
            # form =  BlogForm(request.POST)
            id = request.POST.get('user_info')
            print id
            User.objects.get(id=id).delete()
            return HttpResponseRedirect('/list')










