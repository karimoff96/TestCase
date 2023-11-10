from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.


class Product(TimeStampedModel, models.Model):
    name = models.CharField(max_length=255, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return self.name
