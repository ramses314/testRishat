from django.db import models
from django.urls import reverse

# Create your models here.

class Item(models.Model):

    CURRENCY_CHOICES = [
        ('$', 'usd'),
        ('€', 'eur')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='product/')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='usd')

    def __str__(self):
        return self.name
