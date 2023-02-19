from django.shortcuts import render
from django.contrib.auth.models import User
from appThree.models import UserInfo
from . import forms
from appThree.forms import NewUser, UserForm, UserProfileInfoForm
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

def registration(request):
    
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid:
            user = user_form.save
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        
        else:
            print(user_form.errors,profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'appThree/registration.html',
                           {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})

def users(request):
    user_list = UserInfo.objects.order_by('first_name')
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