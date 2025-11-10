from django.urls import path
from .views import *

urlpatterns = [
    path('products/', productAPI, name='productAPI'),
    path('users/', userAPI, name='userAPI'),
    path('tags/', tagAPI, name='tagAPI'),
    path('brechos/', brechoAPI, name='brechoAPI'),
]