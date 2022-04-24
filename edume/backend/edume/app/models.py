from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    birth_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' ' + self.surname
