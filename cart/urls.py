from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name= 'cart_add'),
    path('plus/<int:product_id>/', views.cart_plus, name= 'cart_plus'),
    path('minus/<int:product_id>/', views.cart_minus, name= 'cart_minus'),
    path('remove/<int:product_id>/', views.cart_remove, name= 'cart_remove'),
    path('del/', views.cart_del, name='cart_del'),
   	
]