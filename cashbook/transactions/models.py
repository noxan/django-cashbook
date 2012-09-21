from django.contrib.auth.models import User
from django.db import models

from currencies.models import Currency

from cashbook.products.models import Product
from cashbook.merchants.models import Merchant


class Transaction(models.Model):
    owner = models.ForeignKey(User, editable=False)
    date = models.DateField()
    merchant = models.ForeignKey(Merchant)
    products = models.ManyToManyField(Product)
    currency = models.ForeignKey(Currency)
