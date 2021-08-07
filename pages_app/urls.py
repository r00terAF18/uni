from django.urls import path

from .views import *

urlpatterns = [
    path("Page/detail/<int:id>/", page_detail, name="page-detail"),
    path(
        "Page/sub/detail/<int:id>/", sub_menu_page_detail, name="sub-menu-page-detail"
    ),
]
