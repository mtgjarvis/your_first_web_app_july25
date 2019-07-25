"""my_first_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from random import randint
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def home_page(request):
    context = {'name': 'Mark Jarvis'}
    response = render(request,'index.html', context)
    return HttpResponse(response)

def gallery_images(request):
    image_urls = []
    for i in range(6):
        random_number = randint(0,100)
        image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))
    context = {'gallery_image': image_urls}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

def about_me(request):
    context = {
        'skills': ['Surfing', 'Coding', 'Cooking'],
        'interests': ['Reading', 'Science', 'Politics', 'Art']
        }
    response = render(request, 'about_me.html', context)
    return HttpResponse(response)


urlpatterns = [
    path('home/', home_page),
    path('portfolio/', gallery_images),
    path('about_me/', about_me),
]
