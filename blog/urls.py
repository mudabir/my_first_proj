from django.conf.urls import url, include
from django.contrib import admin
from blogs.views import *
admin.autodiscover()
urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),
    url(r'^create/$',createUserView.as_view(),name='userCreationURL'),
    url(r'^$',BlogView.as_view(),name='userListURL'),
    url(r'^list/$',BlogView.as_view(),name='userListURL'),
    url(r'^delete/(?P<user_id>.+)/$',DeleteView.as_view(),name='userDeleteURL'),
    url(r'^userprofile/$',UserProfileView.as_view(), name='userProfileURL'),
    url(r'^createprofile/$',CreateUser.as_view(), name='createProfileURL'),
    url(r'^productpurchase/$',ProductPurchaseView.as_view(), name='productpurchaseURL'),
    url(r'^createproduct/$',CreateProductView.as_view(), name='createproductURL'),
    url(r'^products/$',ProductsView.as_view(), name='productURL'),
    url(r'^userregistration/$',UserRegisterationView.as_view(), name='userregisterURL'),
    url(r'^Users_list/$',UsersView.as_view(), name='Users_listURL'),
    url(r'^login/$',LoginView.as_view(),name='LoginURL'),
    url(r'^register/$', RegisterView.as_view(), name='RegisterURL'),


]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)