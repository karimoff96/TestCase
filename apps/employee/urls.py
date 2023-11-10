from django.urls import path
from .views import EmployeeLitsAPIView, EmployeeRetrieveAPIViewAPIView

urlpatterns = [
    path('statistics/', EmployeeLitsAPIView.as_view()),
    path('statistics/employee/<int:id>/',
         EmployeeRetrieveAPIViewAPIView.as_view()),
]
