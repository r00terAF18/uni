from django.shortcuts import get_object_or_404, render
from sidebar_app.models import Sidebar

from .models import Conference


def conference_all(request):
    c = Conference.objects.all().filter(draft=True)
    return render(request, "conference-all.html", {"conferences": c, "txt": "آموزش"})


def conference_detail(request, title):
    c = get_object_or_404(Conference, title=title)
    sidebar = Sidebar.objects.all().filter(sidebar_on_page="Conference").first()
    return render(request, "conference-detail.html", {"c": c, "sidebar": sidebar})
