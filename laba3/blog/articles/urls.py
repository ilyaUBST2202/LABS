# lab3/blog/articles/urls.py

from django.urls import path
from . import views # Импортируем представления из текущего приложения

app_name = 'articles' # Это хорошая практика для пространств имен URL
urlpatterns = [
            # Пустой путь внутри приложения будет направлять на представление archive
            path('', views.archive, name='archive'),
        ]
