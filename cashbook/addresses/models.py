from django.db import models
from django.utils.translation import ugettext_lazy as _

class Country(models.Model):
    name = models.CharField(_("Name"), max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")


class State(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    country = models.ForeignKey(Country, verbose_name=_("Country"))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")


class City(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    zipcode = models.PositiveIntegerField(_("ZIP Code"))
    state = models.ForeignKey(State, verbose_name=_("State"))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")


class Address(models.Model):
    street = models.CharField(_("Street"), max_length=255)
    street_number = models.PositiveSmallIntegerField(_("Street number"))
    city = models.ForeignKey(City, verbose_name=_("City"))

    def __unicode__(self):
        return u'%s,  %s %s' % (self.city.name, self.street, self.street_number)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
