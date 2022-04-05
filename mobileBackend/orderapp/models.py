from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.FloatField()
    quantity_in_stock = models.IntegerField()

    def __str__(self):
        return self.name
