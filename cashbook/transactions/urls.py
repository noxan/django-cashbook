from django.conf.urls import patterns, url

from views import TransactionCreateView, TransactionListView


urlpatterns = patterns('',
    url(r'^$', TransactionListView.as_view(), name='home'),
    url(r'^create/$', TransactionCreateView.as_view(), name='create'),
)
