

from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render



def home_page(request):
    context = {'name': 'Mark Jarvis'}
    response = render(request,'index.html', context)
    return HttpResponse(response)

def root(request):
    return HttpResponseRedirect('home')

def gallery(request):
    return HttpResponseRedirect('portfolio')

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

