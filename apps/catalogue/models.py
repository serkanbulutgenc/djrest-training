from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class BaseProduct:
    def __init__(self, title, price, description):
        self.title = title 
        self.price = price 
        self.description = description

class Product(models.Model):
    title = models.CharField('title', max_length=100, help_text=_('Product title'))
    slug = models.SlugField('slug', unique=True, allow_unicode=True, help_text=_('Product slug'))
    price = models.DecimalField('price', max_digits=8, decimal_places=2, help_text=_('Product price'))
    discount_price = models.DecimalField('discount_price', max_digits=8, decimal_places=2,blank=True, null=True, help_text=_('Discount price'))
    description = models.TextField('description', max_length=1000, help_text=_('Product description'))
    created_at=models.DateTimeField('created_at', auto_now_add=True , editable=False)
    updated_at=models.DateTimeField('updated_at', auto_now=True, editable=False)

    def __str__(self):
        return f'{self.title}'
     
    def get_absolute_url(self):
        pass
