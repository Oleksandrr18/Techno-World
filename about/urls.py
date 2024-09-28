from django.urls import path
from .views import about_pages


urlpatterns = [
    path('', about_pages, name='about')
]
