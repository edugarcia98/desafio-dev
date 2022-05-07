from datetime import datetime
from django.utils.timezone import make_aware


MOCKED_FILE_TO_DICT = [
    {
        "transaction_type": 1,
        "occurrence_date": make_aware(datetime(2022, 2, 2, 1, 1, 1)),
        "value": 15.5,
        "cpf": "99999999999",
        "card": "1234****5678",
        "store_owner": "Foo",
        "store_name": "Bar",
    },
]
