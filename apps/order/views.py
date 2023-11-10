from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from .models import Order
from .serializers import (
    CustomPageNumberPagination,
    OrderSerializer
)

# Create your views here.


class OrderLitsAPIView(ListAPIView):
    queryset = Order.objects.all().order_by("-pk")
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["full_name", 'birthdate']
    filterset_fields = ["full_name", 'birthdate']
    pagination_class = CustomPageNumberPagination


class OrderRetrieveAPIViewAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer