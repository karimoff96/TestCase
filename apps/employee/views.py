from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from .models import Employee
from .serializers import (
    CustomPageNumberPagination,
    EmployeeSerializer
)



class EmployeeLitsAPIView(ListAPIView):
    queryset = Employee.objects.all().order_by("-pk")
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["full_name", 'birthdate']
    filterset_fields = ["full_name", 'birthdate']
    pagination_class = CustomPageNumberPagination


class EmployeeRetrieveAPIViewAPIView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer