from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Sum
from apps.employee.models import Employee
from apps.employee.serializers import EmployeeStatisticsSerializer

class EmployeeStatisticsAPIView(APIView):
    def get(self, request, id=None, *args, **kwargs):
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')

        queryset = Employee.objects.annotate(
            client_count=Count('orders__client', distinct=True),
            product_count=Count('orders__products', distinct=True),
            total_sales=Sum('orders__price')
        )

        if id:
            queryset = queryset.filter(id=id)

        if month and year:
            queryset = queryset.filter(orders__date__month=month, orders__date__year=year)

        serializer = EmployeeStatisticsSerializer(queryset, many=True)
        return Response(serializer.data)