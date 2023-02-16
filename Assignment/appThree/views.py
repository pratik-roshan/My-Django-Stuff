from django.shortcuts import render
from appThree.models import User
from . import forms
from appThree.forms import NewUser
# Create your views here.

def index(request):
    return render(request,'appThree/index.html')

def signup(request):

    form = NewUser()

    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
        else:
            print('ERROR FORM INVALID')

    return render(request,'appThree/signup.html',{'form':form})


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'appThree/users.html',context=user_dict)

# def form_name_view(request):
#     form = forms.FormName()

#     if request.method == 'POST':
#         form = forms.FormName(request.POST)

#         if form.is_valid():
#             print("VALIDATION SUCCESS!")
#             print("NAME: "+form.cleaned_data['name'])
#             print("EMAIL: "+form.cleaned_data['email'])
#             print("TEXT: "+form.cleaned_data['text'])


#     return render(request,'appThree/form_page.html',{'form':form})

def relative(request):
    return render(request,'appThree/relative_url_template.html')