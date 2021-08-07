import json

from django.contrib import messages
from django.shortcuts import redirect, render

from sidebar_app.models import Sidebar, SidebarItem


def sidebar_create(request):
    return render(request, "sidebar/sidebar-create.html")


def sidebar_all(request):
    context = {"sidebars": Sidebar.objects.all()}
    return render(request, "sidebar/sidebar-all.html", context)


def sidebar_submit(request):
    if request.method == "POST":
        data = json.loads(request.body)

        sidebar_title = data.get("sidebar_title")
        sidebar_page = data.get("sidebar_page")

        sidebar_titles = data.get("sidebar_item_title")
        sidebar_links = data.get("sidebar_item_link")

        sidebar = Sidebar.objects.create(
            sidebar_title=sidebar_title, sidebar_on_page=sidebar_page
        )
        sidebar.save()

        for i in range(len(sidebar_titles)):
            s = SidebarItem.objects.create(
                sidebar=sidebar,
                sidebar_item_title=sidebar_titles[i],
                sidebar_link=sidebar_links[i],
            )
            s.save()

        messages.add_message(
            request, messages.SUCCESS, f"Sidebar {sidebar_title} added successfully"
        )

        print(messages)

        return redirect("sidebar-all")


def sidebar_edit(request, id):
    sidebar = Sidebar.objects.get(pk=id)
    items = []

    for s in SidebarItem.objects.all().filter(sidebar=sidebar):
        items.append(s)

    context = {"sidebar": sidebar, "sidebar_items": items}
    return render(request, "sidebar/sidebar-edit.html", context)


def sidebar_update(request):
    if request.method == "POST":
        data = json.loads(request.body)

        id = data.get("id")
        sidebar_title = data.get("sidebar_title")
        sidebar_page = data.get("sidebar_page")

        sidebar_titles = data.get("sidebar_item_title")
        sidebar_links = data.get("sidebar_item_link")

        sidebar = Sidebar.objects.get(
            pk=id, sidebar_title=sidebar_title, sidebar_on_page=sidebar_page
        )
        # empty sidebar_items
        for s in SidebarItem.objects.all().filter(sidebar=sidebar):
            s.delete()

        for i in range(len(sidebar_titles)):
            s = SidebarItem.objects.create(
                sidebar=sidebar,
                sidebar_item_title=sidebar_titles[i],
                sidebar_link=sidebar_links[i],
            )
            s.save()

        sidebar.save()

        messages.add_message(request, 10, f"Sidebar {sidebar_title} added successfully")
        print(messages)

        return redirect("sidebar-all")


def sidebar_delete(request, id):
    sidebar = Sidebar.objects.get(pk=id)
    for ss in SidebarItem.objects.all().filter(sidebar=sidebar):
        ss.delete()

    sidebar.delete()

    return redirect("sidebar-all")
