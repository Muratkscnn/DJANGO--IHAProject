from django.db import models


class ihacat(models.Model):
    brand = models.CharField(max_length=100)
    modelname =models.CharField(max_length=100)
    weight =models.FloatField()
    categories=models.CharField(max_length=100)
    img = models.ImageField(upload_to="static/images")
    description = models.TextField(max_length=500)


    