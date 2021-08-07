# from django.contrib import admin
from baton.autodiscover import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("baton/", include("baton.urls")),
    path("Admin-Panel/", include("adminpanel.urls")),
    path("Newsletter/", include("newsletter.urls")),
    path("", include("core.urls")),
    path("", include("professor_app.urls")),
    path("", include("pages_app.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
