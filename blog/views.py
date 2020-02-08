from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


context = {
    "posts" : Post.objects.all(),
    "projectTitle" : "ProjectIO",
}


def home(request) :

    return render(request, "blog/home.html", context)


def store(request) :
    return render(request, "blog/store.html", context)