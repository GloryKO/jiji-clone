from django.shortcuts import render
from rest_framework import generics,permissions, serializers
from jiji.models import *
from .serializers import *
from .permissions import IsSellerOrReadOnly


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class =ProductSerializer


class ProductDetailView(generics.RetrieveDestroyAPIView):
    permission_classes =(IsSellerOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class InterestView(generics.ListAPIView):
    queryset = Interests.objects.all()
    serializer_class = InterestSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

