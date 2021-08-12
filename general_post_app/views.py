from django.shortcuts import get_object_or_404, render
from sidebar_app.models import Sidebar

from .models import Info


def info_all(request):
    info = Info.objects.all().filter(draft=True)
    return render(request, "info-all.html", {"infos": info})


def info_detail(request, title):
    info = get_object_or_404(Info, title=title)
    sidebar = Sidebar.objects.all().filter(sidebar_on_page="News").first()
    return render(request, "info-detail.html", {"info": info, "sidebar": sidebar})
