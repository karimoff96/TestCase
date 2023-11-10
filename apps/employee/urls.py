from django.urls import path
from .views import EmployeeStatisticsAPIView, EmployeeStatisticsAPIView

urlpatterns = [
    path('statistics/employee/<int:id>/', EmployeeStatisticsAPIView.as_view(), name='employee-statistics-detail'),
    path('statistics/', EmployeeStatisticsAPIView.as_view(), name='employee-statistics'),
]
