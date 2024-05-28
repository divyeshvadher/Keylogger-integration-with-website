# urls.py
from django.urls import path
from .views import register, log_keys

urlpatterns = [
    path('register/', register, name='register'),
    path('log_keys/', log_keys, name='log_keys'),
]
