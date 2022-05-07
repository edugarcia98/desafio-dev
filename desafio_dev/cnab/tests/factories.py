from datetime import datetime

from cnab import TransactionTypeState
from cnab.models import Transaction, TransactionType
from django.utils.timezone import make_aware
from factory.django import DjangoModelFactory


class TransactionTypeFactory(DjangoModelFactory):
    title = "foo"
    state = TransactionTypeState.ENTRY

    class Meta:
        model = TransactionType


class TransactionFactory(DjangoModelFactory):
    occurrence_date = make_aware(datetime(2022, 2, 2, 1, 1, 1))
    value = 15.5
    cpf = "9999999999"
    card = "1234********5678"
    store_owner = "Foo"
    store_name = "Bar"

    class Meta:
        model = Transaction
