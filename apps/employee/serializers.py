from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class EmployeeStatisticsSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField(source='id')
    full_name = serializers.CharField()
    client_count = serializers.IntegerField()
    product_count = serializers.IntegerField()
    total_sales = serializers.DecimalField(max_digits=10, decimal_places=2)
