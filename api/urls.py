from django.urls import path

from . import views

app_name='api'

urlpatterns=[
    path('products/<int:pk>/', views.ProductDetailView.as_view()),
    path('products/', views.products),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view()),
    path('categories/', views.categories),

]