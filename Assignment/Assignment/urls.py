"""Assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from appThree import views

urlpatterns = [
    path("",include('appThree.urls')),
    path("admin/", admin.site.urls),
    path("userinfo", include('appThree.urls')),
    path("users", include('appThree.urls')),
    path("registration/", include('appThree.urls')),
    path("register/", include('appThree.urls')),
    path("login", include('appThree.urls')),
    path("logout", include('appThree.urls')),
    path("relative/", include('appThree.urls')),
    path("form",include('appThree.urls')),
    # path("form/",views.form_name_view,name='form_name')
]
