
from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/second/">Birinchi sayt</a><br><br><button>Next</button>')


def second(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/uch/">ikkinchi sayt</a><br><br><button>Next</button>')


def uch(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/tort/">Uchinchi sayt</a><br><br><button>Next</button>')



def tort(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/besh/">Tort sayt</a><br><br><button>Next</button>')

def besh(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/olti/">Besh sayt</a><br><br><button>Next</button>')

def olti(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/yetti/">OLti sayt</a><br><br><button>Next</button>')

def yetti(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/sakkiz/">Tetti sayt</a><br><br><button>Next</button>')


def sakkiz(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/toqqiz/">Sakkiz sayt</a><br><br><button>Next</button>')

def toqqiz(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/on">Toqqiz sayt</a><br><br><button>Next</button>')


def on(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/">On sayt</a><br><br><button>Home</button>')
