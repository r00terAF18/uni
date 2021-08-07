from .models import Menu, SubMenuPage, SubMenu


def all_menus(request):
    return {"all_menus": Menu.objects.all()}


def all_pages(request):
    return {"all_pages": SubMenuPage.objects.all()}


def all_sub_menus(request):
    return {"all_sub_menus": SubMenu.objects.all()}
