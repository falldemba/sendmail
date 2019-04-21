from django.shortcuts import render, redirect

# Create your views here.


def login(request):
    return render(request,'login.html')

    
def home(request):
    return render(request,'home.html')