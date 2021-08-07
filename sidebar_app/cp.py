from .models import SidebarItem


def list_si(request):
    return {"list_si": SidebarItem.objects.all()}
