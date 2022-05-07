import logging

from datetime import datetime
from typing import List

from cnab.models import Transaction, TransactionType
from django.utils.timezone import make_aware

logger = logging.getLogger(__name__)


def convert_file_to_dict(file: str) -> List[dict]:
    logger.info("Converting file to dict")

    data = []

    for line in file.split("\r\n"):
            if not line:
                continue

            data.append(
                {
                    "transaction_type": int(line[0:1].strip()),
                    "occurrence_date": make_aware(
                        datetime.strptime(
                            f"{line[1:9].strip()} - {line[42:48].strip()}",
                            "%Y%m%d - %H%M%S"
                        )
                    ),
                    "value": float(line[9:19].strip()) / 100.0,
                    "cpf": line[19:30].strip(),
                    "card": line[30:42].strip(),
                    "store_owner": line[48:62].strip(),
                    "store_name": line[62:81].strip(),
                }
            )
    
    return data


def save_file_data(data: List[dict]):
    logger.info("Saving file data.")

    for item in data:
        transaction_type_id = item.pop("transaction_type", None)

        try:
            transaction_type = TransactionType.objects.get(id=transaction_type_id)
            Transaction.objects.create(
                transaction_type=transaction_type, **item,
            )

            message = (
                f"Transaction {item} created with success. "
                f"[Transaction Type ID: {transaction_type_id}]"
            )
            logger.info(message)
        except Exception as exc:
            error_name = type(exc).__name__

            message = (
                f"{error_name} raised unexpectedly while saving {item} to Transaction. "
                f"[Transaction Type ID: {transaction_type_id}] [Content: {exc}]"
            )
            logger.error(message)
