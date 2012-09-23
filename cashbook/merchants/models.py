from django.db import models
from django.utils.translation import ugettext_lazy as _

from cashbook.addresses.models import Address


class Merchant(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    website = models.URLField(_("Website"), blank=True)
    address = models.ForeignKey(Address, verbose_name=_("Address"), blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("Merchant")
        verbose_name_plural = _("Merchants")
