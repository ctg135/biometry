from django.shortcuts import render
from django.views.generic import View

def index(request):
    return render(request, 'main/index.html')

def login(request):
    return render(request, 'main/login.html')

def registration(request):
    return render(request, 'main/registration.html')

def FA2_login(request):
    login_user = request.POST["login"]
    password_user = request.POST["password"]
    print(login_user)
    print(password_user)
    return render(request, "main/2FA_login.html")

def FA2_registartion(request):
    login_user = request.POST["login"]
    password_user = request.POST["password"]
    print(login_user)
    print(password_user)
    return render(request, "main/2FA_registration.html")

def complete_registration(request):
    return render(request, "main/complete_registration.html")

def gis(request):
    return render(request, "main/GIS.html")