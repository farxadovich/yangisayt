
from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/second/">Salom Guruh!</a>')


def second(request):
    return HttpResponse('Xayr guruh!<button>Button</button>')