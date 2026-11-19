from django.urls import path
from .views import CategoryListCreateAPIVIew,CategoryDetailsAPIView

urlpatterns = [
    # views.py তৈরি করার পর আমরা এখানে path() যুক্ত করব
    path('categories/',CategoryListCreateAPIVIew.as_view(),name='category-list-create'),
    path('categories/<int:pk>/',CategoryDetailsAPIView.as_view(),name='category-detail'),
    
]