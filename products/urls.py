from .views import *
from django.urls import path

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', ProductsCategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', ProductsCategoryDetailView.as_view(), name='category-detail'),
    path('makers/', MakerListView.as_view(), name='maker-list'),
    path('makers/<int:pk>/', MakerDetailView.as_view(), name='maker-detail'),
]
