from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def index(request):
    return render(request, 'frontend/index.html')


def register(request):
    form = CreateUserForm()
    form2 = ProfileForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form2 = ProfileForm(request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save()

            profile = form2.save(commit=False)
            profile.user = user

            profile.save()
            messages.success(request, 'Registered successfully')
            return redirect('login')

    context = {'form': form,
               'form2': form2,
               }

    return render(request, 'frontend/register.html', context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'frontend/login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('login')