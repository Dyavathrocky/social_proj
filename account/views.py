from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import login_required

from .forms import LoginForm , UserRegistrationForn, UserEditForm , ProfileEditForm

from .models import Profile
from django.contrib import messages



# Create your views here.

def user_login(request):
    if request.method == "POST": # set request it for POST
        form = LoginForm(request.POST) # call form with instance
        if form.is_valid():  #check the given fields is valid with form class defination 
            cd = form.cleaned_data # loading data to cd variable using cleaned data method
            user = authenticate(request, username=cd['username'], password=cd['password']) #nauthencticate(request , username = " ", password ="password")
            if user is not None: # if user not none
                if user.is_active: # check for his activtie or not , if yes go for login , if not exit
                    login(request, user)
                    return HttpResponse('Autheticated successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse("invalid login")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form })


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html' , {'section':'dashboard'})


def register(request):
    if request.method == "POST":
        a_form = UserRegistrationForn(request.POST)
        if a_form.is_valid():
            new_user = a_form.save(commit=False)
            new_user.set_password(a_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html' , {'new_user': new_user})

    else:
        a_form = UserRegistrationForn()
    return render(request, 'account/register.html',{'form':a_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
          messages.error(request, 'Error updating your profile')  
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance= request.user.profile)

    return render(request, 'account/edit.html', {'user_form':user_form , 'profile_form':profile_form})
            


