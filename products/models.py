from django.db import models

# Create your models here.
class Products(models.Model):
    Product_name = models.CharField(max_length=100)
    Product_image = models.TextField(max_length=1000)
    Product_price = models.CharField(max_length=100)
    class Meta:
        db_table = 'products'

class ProductAdmin(models.Model):
    Product_name = models.CharField(db_column='Product_name', max_length=100, blank=False)
    Product_image = models.TextField(db_column='Product_image', max_length=1000, blank=False)
    Product_price = models.CharField(db_column='Product_price', max_length=100, blank=False)

    class Meta:
        db_table = 'ProductAdmin'
        verbose_name = 'ProductAdmin'
        verbose_name_plural = 'ProductAdmins'

        def __unicode__(self):
            return self.Product_name
        def __str__(self):
            return self.Product_name

class Checkout(models.Model):
    Transactionid = models.CharField(db_column='Transactionid', max_length=100, blank=False)
    amount = models.CharField(db_column='amount', max_length=100, blank=False)
    phone = models.CharField(db_column='phone', max_length=100, blank=False)

    class Meta:
        db_table = 'checkout'
        verbose_name = 'checkout'
        verbose_name_plural = 'checkouts'

        def __unicode__(self):
            return self.Transactionid
        def __str__(self):
            return self.Transactionid