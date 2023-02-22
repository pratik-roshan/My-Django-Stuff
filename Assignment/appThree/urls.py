from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from appThree import views

# TEMPLATE TAGGING
app_name = 'appThree'

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='USERS'),
    path('userinfo', views.UserInfoList.as_view()),
    path('register/', views.signup, name='register'),
    path('registration/', views.registration, name='registration'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('relative/', views.relative, name='relative'),
    path('form', views.form_name_view, name='Forms'),
]