from datetime import datetime

from sidebar_app.models import Sidebar
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

from .models import Departmant, DepForms, DepLab, Professor, ProfessorUpload


def professor_all(request):
    prof = Professor.objects.all()
    return render(request, "Ostad-List.html", {"Prof": prof})


def prof_detail(request, name):
    u = User.objects.get(first_name=name)
    prof = get_object_or_404(Professor, p_user=u)
    pupload = ProfessorUpload.objects.all().filter(p_professor=prof).first()
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sidebar = Sidebar.objects.all().filter(sidebar_on_page="Ostad").first()
    return render(
        request,
        "Ostad-Page.html",
        {"p": prof, "pupload": pupload, "date": dt, "sidebar": sidebar},
    )


def dp_view(request, name):
    d = get_object_or_404(Departmant, name=name)
    dp_forms = DepForms.objects.all().filter(dep=d)
    dp_labs = DepLab.objects.all().filter(dep=d)
    p = Professor.objects.all().filter(target_dep=d)
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
