from unittest.mock import patch, MagicMock

from cnab.models import Transaction, TransactionType
from cnab.tests import MOCKED_FILE_TO_DICT
from cnab.tests.factories import TransactionFactory, TransactionTypeFactory
from cnab.views import load_operations, upload_file
from django.http import Http404
from django.test import TestCase


class TestUploadFile(TestCase):
    def setUp(self):
        self.cnab_file = MagicMock(read=MagicMock("foobar123"))

    @patch("cnab.views.render")
    def test_upload_file_file_not_found(self, mocked_render):
        request = MagicMock(FILES={})

        upload_file(request)

        mocked_render.assert_called_with(
            request, "cnab/upload_file.html", context={"cnab_file": None},
        )

    @patch("cnab.views.save_file_data")
    @patch("cnab.views.convert_file_to_dict")
    @patch("cnab.views.render")
    def test_upload_file_file_found(
        self, mocked_render, mocked_file_to_dict, mocked_save_data,
    ):
        mocked_file_to_dict.return_value = MOCKED_FILE_TO_DICT
        mocked_save_data.return_value = True

        request = MagicMock(FILES={"cnab-file": self.cnab_file})

        upload_file(request)

        mocked_render.assert_called_with(
            request, "cnab/upload_file.html", context={"cnab_file": self.cnab_file},
        )


class TestLoadOperations(TestCase):
    def setUp(self):
        self.transaction_type = TransactionTypeFactory()
        self.transaction = TransactionFactory(transaction_type=self.transaction_type)

        self.request = MagicMock()
        self.slug = "bar"
    
    def test_load_operations_not_found(self):
        with self.assertRaises(Http404) as exc:
            load_operations(self.request, "wrong-slug")
        
        self.assertEqual(str(exc.exception), "wrong-slug NOT FOUND")

    @patch("cnab.views.render")
    def test_load_operations_found(self, mocked_render):
        load_operations(self.request, self.slug)

        context = mocked_render.mock_calls[0][2]["context"]

        self.assertEqual(
            mocked_render.mock_calls[0][1], (self.request, "cnab/operations.html"),
        )
        self.assertEqual(context["store_name"], self.transaction.store_name)
        self.assertEqual(context["store_owner"], self.transaction.store_owner)
        self.assertEqual(context["cpf"], self.transaction.cpf)
        self.assertEqual(context["balance"], self.transaction.value)
