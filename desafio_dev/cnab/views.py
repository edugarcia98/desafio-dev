import logging

from cnab.models import Transaction
from cnab.usecases import convert_file_to_dict, save_file_data
from django.http import Http404, HttpResponse
from django.shortcuts import render


logger = logging.getLogger(__name__)


def upload_file(request):
    if cnab_file := request.FILES.get("cnab-file"):
        message = f"Loaded {cnab_file}"
        logger.info(message)

        file = cnab_file.read().decode("utf-8")
        
        data = convert_file_to_dict(file)
        save_file_data(data)
        

    return render(
        request,
        "cnab/upload_file.html",
        context={"cnab_file": cnab_file}
    )


def load_operations(request, slug):
    queryset = Transaction.objects.filter(slug=slug).order_by("occurrence_date")

    if not queryset.exists():
        raise Http404(f"{slug} NOT FOUND")
    
    balance = 0.0
    for item in queryset:
        item_value = item.value if item.transaction_type.state == "+" else (-item.value)
        balance += item_value
    
    owner_data = queryset[0]
    
    return render(
        request,
        "cnab/operations.html",
        context={
            "store_name": owner_data.store_name,
            "store_owner": owner_data.store_owner,
            "cpf": owner_data.cpf,
            "balance": balance,
            "queryset": queryset
        },
    )
