from core.models import Lecture
from django.shortcuts import redirect, render

from .forms import LectureForm


def lecture_admin_all(request):
    l = Lecture.objects.all()
    return render(request, "lecture/lecture-all.html", {"lectures": l})


def lecture_create(request):
    if request.method == "POST":
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("lecture-admin-all")
    else:
        form = LectureForm()
        return render(request, "lecture/lecture-create.html", {"form": form})


def lecture_edit(request, id):
    l = Lecture.objects.get(pk=id)
    if request.method == "POST":
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("lecture-admin-all")
    else:
        form = LectureForm(instance=l)
        return render(request, "lecture/lecture-create.html", {"form": form, "l": l})


def lecture_delete(request, id):
    l = Lecture.objects.get(pk=id)
    l.delete()
    return redirect("lecture-admin-all")
