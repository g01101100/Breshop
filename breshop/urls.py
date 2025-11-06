from django.urls import path
from .views import *

urlpatterns = [
    path('produto/', produtoAPI, name='produtoAPI')
]