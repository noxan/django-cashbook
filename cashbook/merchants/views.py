from django.views.generic import ListView

from cashbook.merchants.models import Merchant


class MerchantListView(ListView):
    model = Merchant

    def get_context_data(self, **kwargs):
        context = super(MerchantListView, self).get_context_data(**kwargs)
        context['callback'] = self.request.GET.get('callback', None)
        return context
