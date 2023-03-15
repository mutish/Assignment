from django.contrib import admin
from .models import ProductAdmin
from .models import Checkout
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ('Product_name', 'Product_image', 'Product_price')

class AdminCheckout(admin.ModelAdmin):
    list_display = ('Transactionid', 'amount', 'phone')

admin.site.register(ProductAdmin,AdminProduct)
admin.site.register(Checkout, AdminCheckout)