from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    name = models.CharField(_("Name"), max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
