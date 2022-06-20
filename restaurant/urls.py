from django.urls import path
from .views import Dashboard
urlpattern = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]