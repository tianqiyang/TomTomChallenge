from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    location = []
    items = []

class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    item_text = models.CharField(max_length=200)
    type = models.TextField()
    number = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=20)