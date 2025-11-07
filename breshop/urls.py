from django.urls import path
from .views import *

urlpatterns = [
    path('produtos/', produtoAPI, name='produtoAPI'),
    path('users/', userAPI, name='userAPI')
]