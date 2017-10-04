from django.conf.urls import url
from django.contrib import admin
from blogs.views import *

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^create/$',createUserView.as_view(),name='userCreationURL'),
    url(r'^$',BlogView.as_view(),name='userListURL'),
    url(r'^list/$',BlogView.as_view(),name='userListURL'),
    url(r'^delete/(?P<user_id>.+)/$',DeleteView.as_view(),name='userDeleteURL'),
    url(r'^userprofile/$',UserProfileView.as_view(), name='userProfileURL')
]
