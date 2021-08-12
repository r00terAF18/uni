from datetime import datetime

from django.shortcuts import get_object_or_404, render
from professor_app.models import Professor
from sidebar_app.models import Sidebar

from .models import Departmant, DepForms, DepLab


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
        "Daneshkadeh.html",
        {
            "d": d,
            "dp_forms": dp_forms,
            "dp_labs": dp_labs,
            "prof": p,
            "date": dt,
            "sidebar": sidebar,
        },
    )
