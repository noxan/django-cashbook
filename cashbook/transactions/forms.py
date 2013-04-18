from datetime import date

from django import forms
from django.forms.extras.widgets import SelectDateWidget

from models import Transaction


class TransactionCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TransactionCreateForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = SelectDateWidget(years=range(1990, date.today().year + 1))

    class Meta:
        model = Transaction
