from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth import authenticate,login,logout

def home_view(request):
    return render(request,'home.html', {})

def login_view(request):
    error_message = None
    form = forms.LoginForm()
    if request.method == 'POST':
        form= forms.LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')
    return render(request, 'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')