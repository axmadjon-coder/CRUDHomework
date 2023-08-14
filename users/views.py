from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from products.models import Products

def home(request):
    product = Products.objects.all()
    return render(request, 'home.html', {'product':product})

def sign_in(request):

    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')     
       
        return render(request, 'login.html', {'form': form})


def sign_out(request):
    logout(request)

    return redirect('login')
