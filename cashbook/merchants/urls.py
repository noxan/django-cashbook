from django.conf.urls import patterns, url

from views import MerchantListView


urlpatterns = patterns('',
    url(r'^$', MerchantListView.as_view(), name='list'),
)
