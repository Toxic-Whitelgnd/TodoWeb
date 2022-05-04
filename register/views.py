import re
from django.shortcuts import render,redirect
from .forms import NewuserForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


#TODO: FOR THE USER WE HAVE TO CREATE A To make  todolist. 

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = NewuserForm(request.POST)
        print(form)
        if form.is_valid():
            print("came for user registration")
            user = form.save()
            login(request,user)
            messages.success(request,"Regestration Successfull")
            return redirect('/')
        else:
            messages.error(request,"Eroor")
            print("password is too common,try new passowrd and give a valid email address")
    
    form = NewuserForm()
    return render(request,'register/register.html',{'form':form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"You are now logged in with the same username ")
                return redirect('/')
            else:
                messages.error(request,"mother fucker")
                print('fk this shit')
        else:
            messages.error(request,"sdfsdf sdfsdf ")
            print('username is wrong or password is wrong')

    form = AuthenticationForm()
    return render(request,'register/login.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('/')