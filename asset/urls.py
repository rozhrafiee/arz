from django.urls import path
from . import views

urlpatterns = [
    path('arz/', views.arz, name='arz'),
]