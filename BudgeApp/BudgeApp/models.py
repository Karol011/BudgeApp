from django.db import models

class Item(models.Model):
    name = models.CharField()
    price = models.DecimalField()

class Receipt(models.Model):
    item = models.ForeignKey(Item,  on_delete=models.SET_NULL())

