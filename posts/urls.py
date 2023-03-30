from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",Home.as_view(), name="home"),
    path("post/<int:pk>/",Detail_page.as_view(),name="Detail page")
   
   
]
