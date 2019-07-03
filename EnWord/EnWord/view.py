# -- coding: utf-8 --
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)
def page_not_found(request):
    return render(request, '404.html')

def server_error(request):
    return render(request, '500.html')