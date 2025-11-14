# lab3/blog/blog/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
            path('admin/', admin.site.urls),
            # Корневой URL проекта теперь будет использовать URL-адреса из articles.urls
            path('', include('articles.urls')),
        ]
