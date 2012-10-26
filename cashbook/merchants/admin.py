from django.contrib import admin

from cashbook.merchants.models import Merchant


class MerchantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

admin.site.register(Merchant, MerchantAdmin)
