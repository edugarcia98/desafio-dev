from django.db.models import TextChoices


class TransactionTypeState(TextChoices):
    ENTRY = "+", "ENTRY"
    EXIT = "-" , "EXIT"
