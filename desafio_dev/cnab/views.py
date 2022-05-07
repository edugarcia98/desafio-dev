import logging

from cnab.usecases import convert_file_to_dict, save_file_data
from django.http import HttpResponse
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
