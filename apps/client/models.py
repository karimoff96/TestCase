from django.db import models
from model_utils.models import TimeStampedModel
# Create your models here.


class Client(TimeStampedModel, models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    birthdate = models.DateField()

    def __str__(self) -> str:
        return self.full_name
