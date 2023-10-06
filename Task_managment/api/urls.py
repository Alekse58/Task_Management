from django.urls import path
from . import views

urlpatterns = [
    # ... Другие URL-пути вашего приложения ...
    path('telegram_webhook/', views.telegram_webhook, name='telegram_webhook'),
]