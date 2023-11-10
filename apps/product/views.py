from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from .models import Product
from .serializers import (
    CustomPageNumberPagination,
    ProductSerializer
)

# Create your views here.


class ProductLitsAPIView(ListAPIView):
    queryset = Product.objects.all().order_by("-pk")
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["full_name", 'birthdate']
    filterset_fields = ["full_name", 'birthdate']
    pagination_class = CustomPageNumberPagination


class ProductRetrieveAPIViewAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
