from django.urls import path
from appThree import views

# TEMPLATE TAGGING
app_name = 'appThree'

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='USERS'),
    path('register/', views.signup, name='registration'),
    path('relative/', views.relative, name='relative'),
    # path('form', views.form_name_view, name='Forms'),
]