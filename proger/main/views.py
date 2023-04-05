from django.shortcuts import render
from django.http import  HttpResponse


def index(request):
    data = {
        'title': 'Главная страница',
        'values': 'Добро пожаловать на сайт!'
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')



