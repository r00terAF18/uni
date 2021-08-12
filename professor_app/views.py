from datetime import datetime

from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from faculty_app.models import Departmant
from sidebar_app.models import Sidebar

from .models import Professor, ProfessorPost, ProfessorUpload


def professor_all(request):
    prof = Professor.objects.all()
    return render(request, "Ostad-List.html", {"Prof": prof})


def prof_detail(request, name):
    u = User.objects.get(first_name=name)
    prof = get_object_or_404(Professor, p_user=u)
    # dep = Departmant.objects.get(head=prof)
    pupload = ProfessorUpload.objects.all().filter(p_professor=prof).first()
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sidebar = Sidebar.objects.all().filter(sidebar_on_page="Ostad").first()
    try:
        dep = get_object_or_404(Departmant, head=prof)
        context = {
            "p": prof,
            "dep": dep,
            "pupload": pupload,
            "date": dt,
            "sidebar": sidebar,
        }
    except Http404 as h:
        context = {"p": prof, "pupload": pupload, "date": dt, "sidebar": sidebar}
    finally:
        pass
    return render(request, "Ostad-Page.html", context)


def all_pp(request):
    pp = ProfessorPost.objects.all()
    return render(request, "all_professor_posts.html", {"posts": pp})

def professor_post(request, title):
    p = ProfessorPost.objects.get(title=title)
    # prof = Professor.objects.get(id=p.professor.id)
    dep = Departmant.objects.get(head=p.professor.id)
    return render(request, "Ostad-Post.html", {"post": p, "dep": dep})

