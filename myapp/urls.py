from django.urls import path
from .views import product_list, product_list_page

urlpatterns = [
    path('api/', product_list, name='product-list'),
    path('', product_list_page, name='product-list-page'),
]
