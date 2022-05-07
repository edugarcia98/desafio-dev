from cnab.models import Transaction, TransactionType
from django.contrib import admin


@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ("title", "state")
    list_filter = ("state",)
    search_fields = ("title",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "transaction_type",
        "store_owner",
        "cpf",
        "store_name",
        "value",
        "card",
        "occurrence_date",
    )
    list_filter = ("transaction_type",)
    search_fields = ("store_owner", "store_name")
    readonly_fields = ("occurrence_date", "slug")
    fieldsets = (
        ("Owner", {"fields": ("store_owner", "cpf", "store_name", "slug")}),
        ("Transaction", {"fields": ("transaction_type", "value", "card")}),
        ("Monitoring", {"fields": ("occurrence_date",)})
    )
