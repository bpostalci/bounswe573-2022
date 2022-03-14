from django.db import models
from django.utils import timezone

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    address = models.TextField(default='')
    birth_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()
