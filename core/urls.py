from django.urls import path

from .views import *
from .views_news import *
from .views_lecture import *

urlpatterns = [
    path("", home_view, name="home_view"),
    path("Event/all/", event_all, name="event-all"),
    path("Lecture/all/", lecture_all, name="lecture-all"),
    path("Lecture/event/all/", lecture_event_all, name="lecture-event-all"),
    path("Notification/all/", notif_all, name="notif-all"),
    path("News/all/", news_all, name="news-all"),
    path("Lecture/<int:id>/", lecture_detail, name="lecture_detail"),
    path("News/<int:id>/", news_detail, name="news_detail"),
    path("search/", search_query, name="search_query"),
    path("no_access/", no_access, name="no_access"),
]
