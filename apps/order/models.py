from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.


class Order(TimeStampedModel, models.Model):
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    products = models.ManyToManyField('product.Product')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.client.full_name}-{self.employee.full_name}-{self.date}"
