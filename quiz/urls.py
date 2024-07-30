from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('quiz/<int:pk>/', views.ExamDetailView.as_view(), name='exam'),
    #path('result',views.marks())
    ]
