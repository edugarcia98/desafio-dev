import logging

from datetime import datetime

logger = logging.getLogger(__name__)


def convert_file_to_dict(file: str) -> dict:
    logger.info("Converting file to dict")

    for line in file.split("\r\n"):
            if not line:
                continue

            data = {
                "transaction_type": int(line[0:1].strip()),
                "datetime_occurrence": datetime.strptime(
                    f"{line[1:9].strip()} - {line[42:48].strip()}",
                    "%Y%m%d - %H%M%S"
                ),
                "value": float(line[9:19].strip()) / 100.0,
                "cpf": line[19:30].strip(),
                "card": line[30:42].strip(),
                "store_owner": line[48:62].strip(),
                "store_name": line[62:81].strip(),
            }
    
    return data
