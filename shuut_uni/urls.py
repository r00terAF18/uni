# from django.contrib import admin
from baton.autodiscover import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from adminpanel.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("baton/", include("baton.urls")),
    path("Newsletter/", include("newsletter.urls")),
    path("login/", professor_login, name="login"),
    path("logout/", professor_logout, name="logout"),
    path("", include("core.urls")),
    path("", include("professor_app.urls")),
    path("", include("pages_app.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
