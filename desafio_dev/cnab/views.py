import logging

from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def upload_file(request):
    if cnab_file := request.FILES.get("cnab-file"):
        message = f"Loaded {cnab_file}"
        logger.info(message)

    return render(
        request,
        "cnab/upload_file.html",
        context={"cnab_file": cnab_file}
    )
