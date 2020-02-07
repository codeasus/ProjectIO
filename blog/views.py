from django.shortcuts import render
from django.http import HttpResponse



def home(request) :
    return HttpResponse("<h1>Hello, MotherFucker!</h1>")


def store(request) :
    return HttpResponse("<h2>Store section</h2>")