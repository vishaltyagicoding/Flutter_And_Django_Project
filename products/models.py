from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres import fields as postgresfield
# Create your models here.
class Products_Category(models.Model):
    name = models.CharField(max_length=100)
    icon_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    parent_category = models.ForeignKey('self',
                                         on_delete=models.CASCADE,
                                         null=True, 
                                        blank=True,
                                         related_name='children_categories')

    def __str__(self):
        return self.name
    
class Maker (models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    class Currency(models.TextChoices):
        USD = 'USD', _('US Dollar')
        EUR = 'EUR', _('Euro')
        GBP = 'GBP', _('British Pound')
        JPY = 'JPY', _('Japanese Yen')
        CNY = 'CNY', _('Chinese Yuan')
        IND = 'IND', _('Indian Rupee')
        AUD = 'AUD', _('Australian Dollar')
    
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)

    maker  = models.ForeignKey(Maker, on_delete=models.CASCADE, related_name='products', null=True, blank=True)

    image1_url = models.URLField(blank=True)
    image2_url = models.URLField(blank=True)
    image3_url = models.URLField(blank=True)
    image4_url = models.URLField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=Currency.choices, default=Currency.USD)
    variants_product_ids = postgresfield.ArrayField(models.IntegerField(null=True, blank=True), blank=True, null=True)
    def __str__(self):
        return f"{self.title} - {self.subtitle} {self.maker.name if self.maker else ''}"
