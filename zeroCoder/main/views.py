from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")

def data(request):
    return HttpResponse("<h2>Здесь будут размещены данные</h2>")

def test(request):
    return HttpResponse("<h2>Это тестовая страница</h2>")

