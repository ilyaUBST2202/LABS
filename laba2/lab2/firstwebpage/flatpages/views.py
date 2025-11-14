# -*- coding: utf-8 -*-
from django.shortcuts import render # <-- Добавляем render

def home(request):
        # render берет request, имя шаблона и необязательный словарь контекста
        return render(request, 'index.html') # <-- Передаем имя шаблона

