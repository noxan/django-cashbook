from django.contrib.auth.models import User
from django.db import models

from currencies.models import Currency

from cashbook.products.models import Product
from cashbook.merchants.models import Merchant


class Transaction(models.Model):
    owner = models.ForeignKey(User, editable=False)
    date = models.DateField()
    merchant = models.ForeignKey(Merchant)
    products = models.ManyToManyField(Product, through='TransactionProduct')
    currency = models.ForeignKey(Currency, default=0)

    def __unicode__(self):
        return u'%s Transaction from %s' % (unicode(self.date), unicode(self.merchant))

class TransactionProduct(models.Model):
    transaction = models.ForeignKey(Transaction)
    product = models.ForeignKey(Product)
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2)
