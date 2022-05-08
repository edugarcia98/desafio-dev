from cnab.models import Transaction, TransactionType
from cnab.tests.factories import TransactionFactory, TransactionTypeFactory
from django.test import TestCase


class TestTransactionTypeModel(TestCase):
    def setUp(self):
        self.transaction_type = TransactionTypeFactory()
    
    def test_str(self):
        self.assertEqual(str(self.transaction_type), self.transaction_type.title)


class TestTransactionModel(TestCase):
    def setUp(self):
        self.transaction_type = TransactionTypeFactory()
        self.transaction = TransactionFactory(transaction_type=self.transaction_type)
    
    def test_str(self):
        expected_str = (
            f"{self.transaction.store_name}: {self.transaction.transaction_type.title} "
            f"{self.transaction.value}"
        )

        self.assertEqual(str(self.transaction), expected_str)
