from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView

from .forms import UniSystemForm

from .models import UniSystem


class UniSystemList(ListView):
    model = UniSystem
    template_name = "uni_system/uni-system-all.html"
    context_object_name = "uni_sys"


def uni_system_create(request):
    if request.method == "POST":
        form = UniSystemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"University System successfully created")
            return redirect("uni-system-all")
        else:
            return redirect("uni-system-create")
    else:
        form = UniSystemForm()
        return render(request, "uni_system/uni-system-create.html", {"form": form})


def uni_system_edit(request, id):
    uni = UniSystem.objects.get(pk=id)
    if request.method == "POST":
        form = UniSystemForm(request.POST, request.FILES, instance=uni)
        if form.is_valid():
            form.save()
            messages.success(request, f"University System {uni} successfully updated")
            return redirect("uni-system-all")
        else:
            return redirect("uni-system-edit")
    form = UniSystemForm(instance=uni)
    return render(
        request, "uni_system/uni-system-edit.html", {"uni": uni, "form": form}
    )


def uni_system_delete(request, id):
    us = UniSystem.objects.get(pk=id)
    us.delete()
    messages.success(request, f"University System {us} successfully deleted")
    return redirect("uni-system-all")
