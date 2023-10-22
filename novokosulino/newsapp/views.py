from django.shortcuts import render

menu = ['на Главную страницу', 'Графики', 'Таблицы']


def index(request):
    return render(request, "newsapp/index.html", {'menu': menu, 'title': 'Главная страница'})


def tables(request):
    return render(request, "newsapp/tables.html", {'menu': menu, 'title': 'Таблицы'})


def charts(request):
    return render(request, "newsapp/charts.html", {'menu': menu, 'title': 'Графики'})
