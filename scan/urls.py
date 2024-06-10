from django.urls import path
from .views import scanner

urlpatterns = [
    path('', scanner, name='scanner'),
]
