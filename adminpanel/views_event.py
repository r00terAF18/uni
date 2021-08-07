from core.models import Event
from django.shortcuts import redirect, render

from .forms import EventForm


def event_admin_all(request):
    e = Event.objects.all()
    return render(request, "event/event-all.html", {"events": e})


def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("event-admin-all")
    else:
        form = EventForm()
        return render(request, "event/event-create.html", {"form": form})


def event_edit(request, id):
    e = Event.objects.get(pk=id)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("event-admin-all")
    else:
        form = EventForm(instance=e)
        return render(request, "event/event-create.html", {"form": form, "e": e})


def event_delete(request, id):
    e = Event.objects.get(pk=id)
    e.delete()
    return redirect("event-admin-all")
