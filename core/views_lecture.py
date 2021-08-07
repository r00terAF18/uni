from django.shortcuts import get_object_or_404, render
from sidebar_app.models import Sidebar
from .models import Lecture


def lecture_all(request):
    lectures = Lecture.objects.all().filter(lecture_type="آموزش", draft=True)
    return render(
        request, "all-links-lectures.html", {"lectures": lectures, "txt": "آموزش"}
    )


def lecture_event_all(request):
    lectures = Lecture.objects.all().filter(lecture_type="همایش", draft=True)
    return render(
        request, "all-links-lectures.html", {"lectures": lectures, "txt": "همایش"}
    )


def lecture_detail(request, id):
    lecture = get_object_or_404(Lecture, id=id)
    sidebar = Sidebar.objects.all().filter(sidebar_on_page="Lecture").first()
    return render(
        request, "single-lecture.html", {"lecture": lecture, "sidebar": sidebar}
    )
