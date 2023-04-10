"""为应用程序testdj定义URL模式"""
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'testdj'
urlpatterns = [
    path('', views.template_test, name='testdj'),
]
