from django.shortcuts import redirect, render
from faculty_app.models import Departmant
from news_app.models import NewsPost

from .forms import NewsForm


def news_admin_all(request):
    n = NewsPost.objects.all()
    return render(request, "news/news-all.html", {"newsposts": n})


def news_create(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("news-admin-all")
    else:
        dep = Departmant.objects.all()
        form = NewsForm()
        return render(request, "news/news-create.html", {"form": form, "dep": dep})


def news_edit(request, id):
    n = NewsPost.objects.get(pk=id)
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("news-admin-all")
    else:
        dep = Departmant.objects.all()
        form = NewsForm(instance=n)
        return render(
            request, "news/news-create.html", {"form": form, "dep": dep, "n": n}
        )


def news_delete(request, id):
    n = NewsPost.objects.get(pk=id)
    n.delete()
    return redirect("news-admin-all")
