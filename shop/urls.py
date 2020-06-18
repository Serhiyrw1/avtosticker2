from django.urls import path
from .import views

app_name = 'shop'

urlpatterns = [
    path('', views.test, name='test'),
#    path('category/<int:pk>/', views.CategoryViews.as_view(), name='category_list'),
#    path('', views.product_list, name='product_list'),
#    path('category/<int:parent_id>/', views.category_list2, name='category_list2'),
    path('category/<slug:slug>/', views.show_category, name='category_list'),
    path('category2/<slug:slug>/', views.category_list_child, name='category_list_child'),
#    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/<slug:slug>/', views.product_detail, name = 'product_detail'),
#    path('product/<int:pk>/', views.ProductViews.as_view(), name = 'product'),
]