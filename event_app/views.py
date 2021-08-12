from django.shortcuts import render

from .models import Event


def event_all(request):
    events = Event.objects.all().filter(draft=True)
    return render(request, "event-all.html", {"events": events})
