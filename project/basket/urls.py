from django.contrib import admin
from django.urls import path, include

from basket import views

app_name = 'basket'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('edit_cart_quantity/', views.edit_cart_quantity, name='edit_cart_quantity'),
    path('cart_delete/', views.cart_delete, name='cart_delete'),
    path('add_product_to_basket/', views.add_product_to_basket, name='add_product_to_basket'),
]
