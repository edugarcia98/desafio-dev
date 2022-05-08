from unittest.mock import patch

from cnab.models import Transaction, TransactionType
from cnab.tests import MOCKED_FILE_TO_DICT
from cnab.tests.factories import TransactionTypeFactory
from cnab.usecases import convert_file_to_dict, save_file_data
from django.test import TestCase


class TestConvertFileToDict(TestCase):
    def setUp(self):
        self.file = (
            "1202202020000001550999999999991234****5678010101Foo           Bar         "
            "\r\n"
        )
    
    def test_convert_file_to_dict(self):
        data = convert_file_to_dict(self.file)

        self.assertEqual(data, MOCKED_FILE_TO_DICT)


class TestSaveFileData(TestCase):
    def setUp(self):
        self.data = MOCKED_FILE_TO_DICT
        
        TransactionTypeFactory(id=1)

    @patch("cnab.usecases.logger.error")
    def test_save_file_data_error(self, mocked_error_log):
        TransactionType.objects.all().delete()

        save_file_data([{"transaction_type": 1}])

        mocked_error_log.assert_called_with(
            (
                "DoesNotExist raised unexpectedly while saving {} to Transaction. "
                "[Transaction Type ID: 1] [Content: TransactionType matching query "
                "does not exist.]"
            )
        )
    
    def test_save_file_data_success(self):
        save_file_data(self.data)

        self.assertEqual(Transaction.objects.count(), 1)

        transaction = Transaction.objects.first()

        self.assertEqual(transaction.value, 15.5)
        self.assertEqual(transaction.cpf, "99999999999")
        self.assertEqual(transaction.card, "1234****5678")
        self.assertEqual(transaction.store_owner, "Foo")
        self.assertEqual(transaction.store_name, "Bar")
