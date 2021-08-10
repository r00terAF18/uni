from datetime import datetime

from sidebar_app.models import Sidebar
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Departmant, DepForms, DepLab, Professor, ProfessorUpload, ProfessorPost


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


def dp_view(request, name):
    d = get_object_or_404(Departmant, name=name)
    dp_forms = DepForms.objects.all().filter(dep=d)
    dp_labs = DepLab.objects.all().filter(dep=d)
    p = []
    for i in d.ostads.all():
        p.append(Professor.objects.get(id=i.id))
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sidebar = Sidebar.objects.all().filter(sidebar_on_page="Daneshkadeh").first()
    return render(
        request,
        "Daneshkadeh/Daneshkadeh.html",
        {
            "d": d,
            "dp_forms": dp_forms,
            "dp_labs": dp_labs,
            "prof": p,
            "date": dt,
            "sidebar": sidebar,
        },
    )
