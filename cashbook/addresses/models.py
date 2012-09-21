from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    zipcode = models.PositiveIntegerField()
    state = models.ForeignKey(State)

    def __unicode__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=255)
    street_number = models.PositiveSmallIntegerField()
    city = models.ForeignKey(City)

    def __unicode__(self):
        return u'%s,  %s %s' % (self.city.name, self.street, self.street_number)
