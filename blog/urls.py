from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('store/', views.store, name = 'blog-store')
]