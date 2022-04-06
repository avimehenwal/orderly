from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.FloatField()
    quantity_in_stock = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField()
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
