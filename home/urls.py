
from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.landing,name="home"),
    path('landing', views.landing,name="home"),
    path('loginuser',views.loginuser,name='login'),
    path('logoutuser',views.logoutuser,name="logout")

]
