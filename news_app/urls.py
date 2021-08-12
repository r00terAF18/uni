from django.urls import path

from .views import *

urlpatterns = [
    path("", home_view, name="home_view"),
    path("News/all/", news_all, name="news-all"),
    path("News/<int:title>/", news_detail, name="news-detail"),
    path("search/", search_query, name="search_query"),
    path("no_access/", no_access, name="no_access"),
]
