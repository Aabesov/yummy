from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=250)
    picture = models.ImageField()
    price = models.IntegerField()
    category = models.CharField(max_length=30)


