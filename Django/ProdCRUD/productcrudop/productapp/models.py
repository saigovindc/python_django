from django.db import models


# Create your models here.

class Product(models.Model):
    p_NAME = models.CharField(max_length=200)
    p_ID = models.IntegerField()
    p_PRICE = models.IntegerField()

    class Meta:
        db_table = 'productdatabase'