from unicodedata import name
from django.urls import path
from . import views

app_name = 'xo'

urlpatterns = [
  path('', views.index, name='index'),
]
