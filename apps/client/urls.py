from django.urls import path
from .views import ClientRetrieveAPIViewAPIView

urlpatterns = [
    path('statistics/client/<int:id>/',
         ClientRetrieveAPIViewAPIView.as_view()),
]
