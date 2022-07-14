from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import CartSerializer
from .models import Cart


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    def perform_create(self, serializer, **kwargs):
        kwargs['user'] = self.request.user
        serializer.save(user=self.request.user)