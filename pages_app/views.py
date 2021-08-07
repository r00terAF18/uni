from django.shortcuts import redirect, render

from .models import Menu, SubMenu, SubMenuPage


def page_detail(request, id):
    page = Menu.objects.get(pk=id)
    return render(request, "page/page-detail.html", {"page": page})


def sub_menu_page_detail(request, id):
    page = SubMenuPage.objects.get(pk=id)
    return render(request, "page/page-detail.html", {"page": page})
