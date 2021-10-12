from django.shortcuts import get_object_or_404, render
from sidebar_app.models import Sidebar

from .models import Lecture


def lecture_all(request):
    lectures = Lecture.objects.all().filter(draft=True)
    return render(request, "lecture-all.html", {"lectures": lectures})


def lecture_detail(request, id):
    lecture = get_object_or_404(Lecture, id=id)
    sidebar = Sidebar.objects.all().filter(sidebar_on_page="Lecture").first()
    return render(
        request, "lecture-detail.html", {"lecture": lecture, "sidebar": sidebar}
    )
