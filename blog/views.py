from django.shortcuts import render
from django.http import HttpResponse



posts = [
    {
        'author' : 'Orhan Rosenfeld',
        'title' : 'Graphic Programming',
        'content' : 'Graphic programming content.',
        'post_date' : 'Febuary 2, 2020'
    },
    {
        'author' : 'Anar Abbasov',
        'title' : 'Machine Learning',
        'content' : 'Machine learning content.',
        'post_date' : 'December 28, 2019'
    }
]

context = {
    "posts" : posts,
    "projectTitle" : "ProjectIO",
}


def home(request) :

    return render(request, "blog/home.html", context)


def store(request) :
    return render(request, "blog/store.html", context)