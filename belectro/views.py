# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'belectro/index.html')


def electric(request):

    return render(request, 'belectro/electric.html')


def heat_and_cold(request):
    return render(request, 'belectro/heat-and-cold.html')


def computers(request):
    return render(request, 'belectro/computers.html')

def aboutus(request):
    return render(request, 'belectro/aboutus.html')

def contact(request):
    return render(request, 'belectro/contact.html')
















