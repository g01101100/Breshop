from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductView.as_view(), name='productView'),
    path('users/', UserView.as_view(), name='View'),
    path('tags/', TagView.as_view(), name='View'),
    path('brechos/', BrechoView.as_view(), name='View'),
    path('addresses/', AddressView.as_view(), name='View'),
]