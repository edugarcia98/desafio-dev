from cnab import TransactionTypeState
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify


class TransactionType(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    state = models.CharField(
        max_length=10, choices=TransactionTypeState.choices, verbose_name="State",
    )

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ("title",)
        verbose_name = "Transaction Type"
        verbose_name_plural = "Transaction Types"


class Transaction(models.Model):
    transaction_type = models.ForeignKey(
        TransactionType,
        on_delete=models.PROTECT,
        null=False,
        verbose_name="Transaction Type",
    )
    occurrence_date = models.DateTimeField(verbose_name="Occurrence Date")
    value = models.FloatField(
        validators=(MinValueValidator(0.0),), verbose_name="Value",
    )
    cpf = models.CharField(max_length=20, verbose_name="CPF")
    card = models.CharField(max_length=20, verbose_name="Card")
    store_owner = models.CharField(max_length=50, verbose_name="Store Owner")
    store_name = models.CharField(max_length=50, verbose_name="Store Name")
    slug = models.SlugField(unique=True)

    def save(self):
        self.slug = slugify(self.store_name)
        super(Transaction, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.store_name}: {self.transaction_type.title} {self.value}"
    
    class Meta:
        ordering = ("store_name",)
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
