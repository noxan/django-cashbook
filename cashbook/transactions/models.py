from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import m2m_changed, post_save, pre_delete
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from currencies.models import Currency

from cashbook.products.models import Product
from cashbook.merchants.models import Merchant


class Transaction(models.Model):
    owner = models.ForeignKey(User, verbose_name=_("Owner"), editable=False)
    date = models.DateField(_("Date"))
    merchant = models.ForeignKey(Merchant, verbose_name=_("Merchant"))
    products = models.ManyToManyField(Product, verbose_name=_("Products"), through='TransactionProduct')
    currency = models.ForeignKey(Currency, verbose_name=_("Currency"), default=0)
    value = models.DecimalField(_("Value"), max_digits=12, decimal_places=2, default=0.0, blank=True, editable=False)
    comment = models.TextField(_("Comment"), blank=True)

    def calculate_value(self, delta=0):
        self.value = delta
        for product in self.transactionproduct_set.all():
            self.value += product.price * product.quantity
        self.save()

    def __unicode__(self):
        return _("%s Transaction from %s") % (unicode(self.date), unicode(self.merchant))

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")


class TransactionProduct(models.Model):
    transaction = models.ForeignKey(Transaction, verbose_name=_("Transaction"))
    product = models.ForeignKey(Product, verbose_name=_("Product"))
    quantity = models.PositiveSmallIntegerField(_("Quantity"), default=1)
    price = models.DecimalField(_("Price"), max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = _("Transaction product")
        verbose_name_plural = _("Transaction products")


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
