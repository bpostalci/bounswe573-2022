from django.db import models
from django.utils import timezone

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    address = models.TextField(default='')
    birth_date = models.DateTimeField(default=timezone.now)
    wd_records = models.ManyToManyField('WDRecord', related_name='wd_records')

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' ' + self.surname


class WDRecord(models.Model):
    wd_id = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return self.wd_id
