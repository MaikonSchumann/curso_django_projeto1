from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request):
    # return HTTP response
    return HttpResponse('Hello World, tudo certo? VIews nova')


def contato_view(request):
    # return HTTP response
    return HttpResponse('Página /CONTATO/')


def sobre_view(request):
    # return HTTP response
    return HttpResponse('Página /SOBRE/')