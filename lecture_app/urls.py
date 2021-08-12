from django.urls import path

from .views import *

urlpatterns = [
    path("Lecture/all/", lecture_all, name="lecture-all"),
    path("Lecture/<str:title>/", lecture_detail, name="lecture-detail"),
]
