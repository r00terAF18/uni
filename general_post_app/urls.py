from django.urls import path

from .views import *

urlpatterns = [
    path("Info/all/", info_all, name="info-all"),
    path("Info/<str:title>/", info_detail, name="info-detail"),
]
