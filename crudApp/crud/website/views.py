from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def login(request):
   return render(request, 'pages/login.html')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')

    context = {"form": form}

    return render(request,"pages/register.html",context=context)
