from django.urls import path

from .views import *

urlpatterns = [
    path("Daneshkadeh/<str:name>/", dp_view, name="dp_view"),
]
