from django.views.generic import ListView

from models import Transaction


class TransactionListView(ListView):
    model = Transaction
