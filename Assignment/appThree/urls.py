from django.urls import path
from appThree import views


urlpatterns = [
    path('users', views.users, name='users'),
    path('', views.index, name='index')
]