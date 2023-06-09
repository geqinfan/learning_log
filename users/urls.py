"""为应用程序users定义URL模式"""
from django.contrib.auth import login
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'
urlpatterns = [
    # 登录页面
    # path('login/', login, {'template_name': 'users/login.html'}, name='login'),
    # path('login/', login, name='login'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('login/', LoginView.as_view, name='login'),
    # 注销页面
    path('logout/', views.logout_view, name='logout'),
    # 注册页面
    path('register/', views.register, name='register'),
]
