from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)


class State(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country)


class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State)


class Address(models.Model):
    street = models.CharField(max_length=255)
    street_number = models.PositiveSmallIntegerField()
    city = models.ForeignKey(City)
