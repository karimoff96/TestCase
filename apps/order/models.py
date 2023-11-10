from django.db import models
from model_utils.models import TimeStampedModel

class Order(TimeStampedModel, models.Model):
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    products = models.ManyToManyField('product.Product')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            super(Order, self).save(*args, **kwargs)
            self.price = self.calculate_order_price()
            super(Order, self).save(*args, **kwargs)
        else:
            self.price = self.calculate_order_price()
            super(Order, self).save(*args, **kwargs)

    def calculate_order_price(self):
        total_price = sum(product.price for product in self.products.all())
        return total_price

    def __str__(self):
        return f"Order {self.id} for {self.client.full_name} by {self.employee.full_name}"
