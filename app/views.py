from django.http import HttpResponse
from django.shortcuts import render, reverse

import datetime
import pytz
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    tz_moscow = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(tz_moscow)
    msg = f'Текущее время: {current_time.strftime("%H:%M")}'
    return HttpResponse(msg)


def workdir_view(request):
    workdir = os.listdir(path='.')
    return HttpResponse(str(workdir))