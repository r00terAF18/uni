from professor_app.models import Departmant, Professor
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .forms import DepForm


class CollegeList(ListView):
    model = Departmant
    template_name = "colleges/college-all.html"
    context_object_name = "dep"


def college_add(request):
    if request.method == "POST":
        form = DepForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("college-all")
    else:
        u = Professor.objects.all()
        print(u)
        form = DepForm()
        return render(
            request, "colleges/college-creator.html", {"user": u, "form": form}
        )


def college_all(request):
    dep = Departmant.objects.all()
    return render(request, "colleges/college-all.html", {"dep": dep})


def college_edit(request, id):
    dep = get_object_or_404(Departmant, pk=id)
    u = User.objects.all()
    form = DepForm()
    return render(
        request, "colleges/college-edit.html", {"user": u, "form": form, "c": dep}
    )


def college_update(request, id):
    if request.method == "POST":
        data = request.POST
        dep = get_object_or_404(Departmant, pk=id)
        dep.name = data["name"]
        dep.head = User.objects.get(pk=data["head"])
        dep.image = request.FILES.get("image")
        dep.info = data["info"]
        dep.save()

    return redirect("college-all")


def college_delete(request, id):
    dep = get_object_or_404(Departmant, pk=id).delete()
    return redirect("college-all")
