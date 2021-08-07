from django.shortcuts import redirect

from .models import Subscriber


def subscribe(request):
    email = request.POST["email_field"]
    sub = Subscriber.objects.create(email=email)
    sub.save()
    return redirect("home_view")
