    # lab3/blog/articles/admin.py

from django.contrib import admin
from .models import Article # Импортируем нашу модель Article

    # Класс ArticleAdmin описывает, как модель Article будет отображаться в административной панели
class ArticleAdmin(admin.ModelAdmin):
        # list_display определяет поля, которые будут отображаться в списке статей
        # 'get_excerpt' вызовет соответствующий метод нашей модели
        list_display = ('title', 'author', 'get_excerpt', 'created_date')

    # Регистрируем модель Article и связываем ее с классом ArticleAdmin
admin.site.register(Article, ArticleAdmin)
