from django.urls import path
from breshop.views import view_address, view_becho, view_product, view_tag, view_user

urlpatterns = [
    path('addresses/', view_address.AddressView.as_view(), name='addressView'),
    path('brechos/', view_becho.BrechoView.as_view(), name='brechoView'),
    path('products/', view_product.ProductView.as_view(), name='productView'),

    path('tags/', view_tag.TagListCreateView.as_view(), name='tagListCreateView'),
    path('tags/<int:pk>', view_tag.TagDatailView.as_view(), name='tagDetaiwlView'),
    
    path('users/', view_user.UserView.as_view(), name='userView'),
]