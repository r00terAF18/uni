import json

from django.http.response import JsonResponse
from django.shortcuts import redirect, render

from .forms import PageForm
from pages_app.models import Menu, SubMenu, SubMenuPage


def page_detail(request, id):
    page = Menu.objects.get(pk=id)
    return render(request, "page/page-detail.html", {"page": page})


def sub_menu_page_detail(request, id):
    page = SubMenuPage.objects.get(pk=id)
    return render(request, "page/page-detail.html", {"page": page})


def header_create(request):
    pc = SubMenuPage.objects.all()
    ids = []
    names = []

    for p in pc:
        ids.append(p.id)
        names.append(str(p))

    return render(
        request,
        "header/header-create.html",
        {"page_content": pc, "ids": ids, "names": names},
    )


def page_submit(request):
    if request.method == "POST":
        data = request.POST

        title = data["page-name"]
        image = request.FILES.get("image-uploader")
        content = data["content"]

        pc = SubMenuPage.objects.create(title=title, image=image, content=content)
        pc.save()

        return redirect("page-all")


def header_multi_submit(request):
    data = json.loads(request.body)

    title = data.get("title")
    ids = data.get("ids")

    sub_menu = SubMenu.objects.create(sub_menu=title)
    sub_menu.save()

    for id in ids:
        page = SubMenuPage.objects.get(pk=id)
        page.sub_menu = sub_menu
        page.save()

    return JsonResponse({"success": True})


def header_single_submit(request):
    data = json.loads(request.body)

    id = data.get("id")

    page = SubMenuPage.objects.get(pk=id)
    menu = Menu.objects.create(
        menu_title=str(page), title=page.title, image=page.image, content=page.content
    )
    menu.save()

    return redirect("page-all")


def page_create(request):
    form = PageForm()
    return render(request, "header/page-create.html", {"form": form})


def page_all(request):
    pc = SubMenuPage.objects.all()
    return render(request, "header/page-all.html", {"page_content": pc})


def page_edit(request, id):
    form = PageForm()
    pc = SubMenuPage.objects.get(pk=id)
    return render(request, "header/page-edit.html", {"pc": pc, "form": form})


def page_update(request, id):
    if request.method == "POST":
        data = request.POST

        title = data["page-name"]
        image = request.FILES.get("image-uploader")
        content = data["content"]

        pc = SubMenuPage.objects.get(pk=id)
        pc.title = title
        pc.image = image
        pc.content = content
        pc.save()

        return redirect("page-all")


def page_delete(request, id):
    pc = SubMenuPage.objects.get(pk=id)
    pc.delete()
    return redirect("page-all")
