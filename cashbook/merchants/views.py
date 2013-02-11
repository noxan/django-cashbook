from django.views.generic import ListView

from models import Merchant


class MerchantListView(ListView):
    model = Merchant
