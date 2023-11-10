from django.urls import path
from .views import ClientStatisticsAPIView

urlpatterns = [
    path('statistics/client/<int:id>/', ClientStatisticsAPIView.as_view(), name='client-statistics-detail'),
]
