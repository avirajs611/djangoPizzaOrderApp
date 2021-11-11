from django.db import models

from django.utils import timezone


class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now, )
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return self.topping1
