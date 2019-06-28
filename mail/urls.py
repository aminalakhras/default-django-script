from django.conf.urls import  url
from django.urls import path
from . import views

urlpatterns = [
    path("mail/", views.index, name="SendMail"),
]
