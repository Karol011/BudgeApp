from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Receipt(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name='items', null=True)
