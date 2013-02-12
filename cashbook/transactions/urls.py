from django.conf.urls import patterns, url

from views import TransactionListView


urlpatterns = patterns('',
    url(r'^$', TransactionListView.as_view(), name='home'),
)
