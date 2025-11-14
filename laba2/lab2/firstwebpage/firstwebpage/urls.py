    # firstwebpage/firstwebpage/urls.py
from django.contrib import admin  # <-- Здесь ошибка!
from django.urls import path
from django.views.generic import TemplateView # Импортируем TemplateView
from django.conf import settings # Для обработки статических файлов в режиме DEBUG
from django.conf.urls.static import static # Для обработки статических файлов в режиме DEBUG
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # Для сбора статики

    # from flatpages import views #  views.home больше не нужна для корневого URL

urlpatterns = [
        path('admin/', admin.site.urls),
        # Изменяем этот путь, чтобы он показывал static_handler.html
        path('', TemplateView.as_view(template_name='static_handler.html'), name='home'),
        # path('hello/', views.home, name='hello'), 
    ]

    # Это ОЧЕНЬ ВАЖНО для того, чтобы статические файлы (CSS, картинки) работали в режиме разработки!
if settings.DEBUG:
        urlpatterns += staticfiles_urlpatterns()
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Если у вас есть MEDIA_URL/MEDIA_ROOT
