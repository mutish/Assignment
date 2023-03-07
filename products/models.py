from django.db import models

# Create your models here.
class Products(models.Model):
    Product_name = models.CharField(max_length=100)
    Product_image = models.URLField()
    Product_price = models.CharField(max_length=1000000)
    class Meta:
        db_table = 'products'

