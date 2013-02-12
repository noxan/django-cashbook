from django.views.generic import CreateView, ListView

from models import Merchant


class MerchantListView(ListView):
    model = Merchant


class MerchantCreateView(CreateView):
    model = Merchant
    template_name = 'merchants/merchant_create.html'
