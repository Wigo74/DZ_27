from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)

