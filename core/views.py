from django.shortcuts import render

def base(request):
    return render(request, 'core/base.html')

def login(request):
    return render(request, 'core/login.html')

def signup(request):
    return render(request, 'core/signup.html')

def about(request):
    return render(request, 'core/about.html')