from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=50, default="aaaa@gmail.com")
    birth_date = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=200, default="123456")

    def publish(self):
        print('yes')
        self.save()

    def __str__(self):
        return self.name + ' ' + self.surname
