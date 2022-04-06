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
    date_created = models.DateField()
    user_id = models.ForeignKey(
        User, related_name='user', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='item', on_delete=models.CASCADE)
