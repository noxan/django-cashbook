from django.contrib import admin

from cashbook.addresses.models import Country, State, City, Street, Address


admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Street)
admin.site.register(Address)
