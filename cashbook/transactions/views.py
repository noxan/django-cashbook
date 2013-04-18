from django.views.generic import CreateView, ListView

from forms import TransactionCreateForm
from models import Transaction


class TransactionListView(ListView):
    model = Transaction


class TransactionCreateView(CreateView):
    model = Transaction
    template_name = 'transactions/transaction_create.html'
    form_class = TransactionCreateForm
