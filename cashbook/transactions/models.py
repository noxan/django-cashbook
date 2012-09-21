from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import m2m_changed, post_save, pre_delete
from django.dispatch import receiver

from currencies.models import Currency

from cashbook.products.models import Product
from cashbook.merchants.models import Merchant


class Transaction(models.Model):
    owner = models.ForeignKey(User, editable=False)
    date = models.DateField()
    merchant = models.ForeignKey(Merchant)
    products = models.ManyToManyField(Product, through='TransactionProduct')
    currency = models.ForeignKey(Currency, default=0)
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0.0, blank=True, editable=False)
    comment = models.TextField(blank=True)

    def calculate_value(self, delta=0):
        self.value = delta
        for product in self.transactionproduct_set.all():
            self.value += product.price * product.quantity
        self.save()

    def __unicode__(self):
        return u'%s Transaction from %s' % (unicode(self.date), unicode(self.merchant))

class TransactionProduct(models.Model):
    transaction = models.ForeignKey(Transaction)
    product = models.ForeignKey(Product)
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2)

@receiver(post_save, sender=TransactionProduct)
def product_saved(sender, instance, created, raw, using, **kwargs):
    instance.transaction.calculate_value()

@receiver(pre_delete, sender=TransactionProduct)
def product_deleted(sender, instance, using, **kwargs):
    instance.transaction.calculate_value()

@receiver(m2m_changed, sender=Transaction.products.through)
def products_changed(sender, instance, action, reverse, model, pk_set, using, **kwargs):
    if action == 'post_add':
        instance.calculate_value()
