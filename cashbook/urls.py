from django.conf.urls import patterns, include, url
from django.contrib import admin

from cashbook.merchants.views import MerchantListView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/merchants.json$', MerchantListView.as_view(), name='merchants'),
    # Examples:
    # url(r'^$', 'cashbook.views.home', name='home'),
    # url(r'^cashbook/', include('cashbook.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
