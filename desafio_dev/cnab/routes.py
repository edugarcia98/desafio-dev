from cnab.views import load_operations, upload_file
from django.urls import path


urlpatterns = [
    path("upload-file/", upload_file, name="upload-file"),
    path("operations/<str:slug>/", load_operations, name="operations")
]
