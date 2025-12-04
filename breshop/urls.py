from django.urls import path
from breshop.views import view_address, view_brecho, view_product, view_tag, view_user, view_login

urlpatterns = [
    path('addresses/', view_address.AddressView.as_view(), name='addressCrateListView'),
    path('addresses/<int:pk>/', view_address.AddressDatailView.as_view(), name='addressDetaiwlView'),
    
    path('brechos/', view_brecho.BrechoView.as_view(), name='brechoView'),
    path('brechos/<int:pk>/', view_brecho.BrechoDatailView.as_view(), name='brechoDetaiwlView'),
    
    path('products/', view_product.ProductView.as_view(), name='productView'),
    path('products/<int:pk>/', view_product.ProductDatailView.as_view(), name='productDetaiwlView'),

    path('tags/', view_tag.TagListCreateView.as_view(), name='tagListCreateView'),
    path('tags/<int:pk>/', view_tag.TagDatailView.as_view(), name='tagDetaiwlView'),
    
    path('users/', view_user.UserView.as_view(), name='userView'),
    path('users/<int:pk>/', view_user.UserDatailView.as_view(), name='userDetaiwlView'),

    path('login/', view_login.login_view, name='loginView'),
    path('me/', view_login.me_view, name='meView'),
]
