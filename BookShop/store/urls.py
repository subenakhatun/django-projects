from django.urls import path,include
from .views import (
    CategoryListCreateAPIVIew,
    CategoryDetailsAPIView,
    AuthorListCreateAPIView,
    AuthorDetailAPIView,
    BookListCreateAPIView,
    BookDetailAPIView,
    BookViewSet,
    AuthorProfileDetailsViewSet,
    
    )
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'v2/books', BookViewSet, basename='book-v2')

urlpatterns = [
    # views.py তৈরি করার পর আমরা এখানে path() যুক্ত করব
    path('categories/',CategoryListCreateAPIVIew.as_view(),name='category-list-create'),
    path('categories/<int:pk>/',CategoryDetailsAPIView.as_view(),name='category-detail'),
    path('profile',AuthorProfileDetailsViewSet.as_view(),name='author-profile-details'),
    path('authors/',AuthorListCreateAPIView.as_view(),name='authors-list-create'),
    path('authors/<int:pk>/',AuthorDetailAPIView.as_view(),name='authors-detail'),
    path('books/',BookListCreateAPIView.as_view(),name='book-list-create'),
    path('books/<int:pk>/',BookDetailAPIView.as_view(),name='book-detail'),
    path('', include(router.urls)),
    
]