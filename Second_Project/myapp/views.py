from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me':"Hello I am coming from Myapp"}
    return render(request, 'myapp/index.html', context=my_dict)

def help(request):
    help_dict = {'help_insert':'Any HELP Required'}
    return render(request, 'myapp/help.html', context=help_dict)

 