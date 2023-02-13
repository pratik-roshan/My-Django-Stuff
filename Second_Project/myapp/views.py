from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    # my_dict = {'insert_me':"Hello I am coming from Myapp"}
    return render(request, 'myapp/index.html', context=date_dict)

def help(request):
    help_dict = {'help_insert':'Any HELP Required'}
    return render(request, 'myapp/help.html', context=help_dict)

 