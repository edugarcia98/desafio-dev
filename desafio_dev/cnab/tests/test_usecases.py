from cnab.tests import MOCKED_FILE_TO_DICT
from cnab.usecases import convert_file_to_dict
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
