from django.urls import path

from .views import *

urlpatterns = [
    path("Event/all/", event_all, name="event-all"),
]
