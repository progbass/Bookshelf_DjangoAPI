from django.conf.urls import include,url
from django.contrib import admin
from .views import CreateUser

urlpatterns = [
    url(r'^$', CreateUser.as_view()),    
]
