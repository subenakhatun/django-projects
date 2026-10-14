from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='shop_home' ),
    path('products/', views.products,name='shop_products' ),
]