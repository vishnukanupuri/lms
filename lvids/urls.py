from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.Home.as_view(),name='home'),

    path('dep',views.Dep.as_view(),name='dep'),

    path('cse',views.Cse,name='cse'),

    path('login',views.LoginInterfaceView.as_view()),

    path('logout',views.LogoutInterfaceView.as_view()),

    path('signup',views.SignupView.as_view()),

    
]
