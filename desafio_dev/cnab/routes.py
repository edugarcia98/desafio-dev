from cnab.views import upload_file
from django.urls import path


urlpatterns = [
    path("upload-file/", upload_file, name="upload-file"),
]
