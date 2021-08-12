# from django.contrib import admin
from adminpanel.views import *
from baton.autodiscover import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("baton/", include("baton.urls")),
    path("Newsletter/", include("newsletter.urls")),
    path("login/", professor_login, name="login"),
    path("logout/", professor_logout, name="logout"),
    path("", include("news_app.urls")),
    path("", include("event_app.urls")),
    path("", include("conference_app.urls")),
    path("", include("lecture_app.urls")),
    path("", include("general_post_app.urls")),
    path("", include("professor_app.urls")),
    path("", include("faculty_app.urls")),
    path("", include("pages_app.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
