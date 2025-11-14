    # lab3/blog/articles/views.py

from .models import Article # Правильный относительный импорт нашей модели
from django.shortcuts import render

def archive(request):
        # Получаем все статьи из базы данных, отсортированные по убыванию даты создания
        all_articles = Article.objects.all().order_by('-created_date')
        # Передаем список статей в шаблон под именем "posts"
        return render(request, 'archive.html', {"posts": all_articles})
