from django.db import models
from model_utils.models import TimeStampedModel


class Order(TimeStampedModel, models.Model):
    client = models.ForeignKey(
        'client.Client', on_delete=models.CASCADE, related_name='orders')
    employee = models.ForeignKey(
        'employee.Employee', on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField('product.Product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} for {self.client.full_name} by {self.employee.full_name}"
