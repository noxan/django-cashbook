from django.conf.urls import patterns, url

from views import MerchantCreateView, MerchantListView


urlpatterns = patterns('',
    url(r'^$', MerchantListView.as_view(), name='list'),
    url(r'^create/$', MerchantCreateView.as_view(), name='create'),
)
