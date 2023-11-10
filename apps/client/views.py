from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Sum
from apps.client.models import Client
from apps.client.serializers import ClientStatisticsSerializer

class ClientStatisticsAPIView(APIView):
    def get(self, request, id=None, *args, **kwargs):
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')

        queryset = Client.objects.annotate(
            product_count=Count('orders__products', distinct=True),
            total_sales=Sum('orders__price')
        )

        if id:
            queryset = queryset.filter(id=id)

        if month and year:
            queryset = queryset.filter(orders__date__month=month, orders__date__year=year)

        serializer = ClientStatisticsSerializer(queryset, many=True)
        return Response(serializer.data)