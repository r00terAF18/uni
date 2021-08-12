from django.urls import path

from .views import *

urlpatterns = [
    path("Conference/all/", conference_all, name="conference-all"),
    path("Conference/<str:title>/", conference_detail, name="conference-detail"),
]
