from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from django.shortcuts import render, redirect, HttpResponse
from .models import Client
from .serializers import (
    CustomPageNumberPagination,
    ClientSerializer
)

# Create your views here.


class ClientLitsAPIView(ListAPIView):
    queryset = Client.objects.all().order_by("-pk")
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["full_name", 'birthdate']
    filterset_fields = ["full_name", 'birthdate']
    pagination_class = CustomPageNumberPagination


class ClientRetrieveAPIViewAPIView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
