from django.contrib import admin
from django.contrib.auth.models import User

from models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.owner
        except User.DoesNotExist:
            obj.owner = request.user
        obj.save()

admin.site.register(Transaction, TransactionAdmin)
