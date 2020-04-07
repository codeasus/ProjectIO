from django.shortcuts import render
from django.http import HttpResponse
           
def signup(request) :
    return render(request, 'welcome/signup.html')

def index(request) :
    return render(request, 'welcome/index.html')