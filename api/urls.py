from django.urls import path
from rest_framework import views
from .views import *

urlpatterns = [
    path('products', ProductListView.as_view()),
    path('products/create/', ProductCreateView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('signup/', RegisterView.as_view()),
]
