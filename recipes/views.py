from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Rodrigo',
    })

def contact(request):
    return HttpResponse("Hello, world. You're at the contact page.")

def about(request):
    return HttpResponse("Hello, world. You're at the about page.")