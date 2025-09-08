from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def login(request):
    form = LoginForm(request, data=request.POST)

    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
           auth.login(request, user)
           return redirect('')
    context = {'login_form':form}
    return render(request, 'pages/login.html', context=context)

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {"form": form}

    return render(request,"pages/register.html",context=context)


def user_logout(request):
    auth.logout(request)
    return redirect("login")

#dashboard
@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'website/dashboard.html')