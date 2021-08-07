from professor_app.models import Professor
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import ProfessorPostForm, ProfessorUploadForm
from professor_app.models import ProfessorPost, ProfessorUpload


def professor_add(request):
    form = ProfessorUploadForm()
    return render(
        request,
        "professor/add-professor-page-contorler.html",
        {"form": form},
    )


def professor_create_user(request):
    if request.method == "POST":
        data = request.POST
        name = data["ostad-first-name"]
        family_name = data["ostad-family-name"]
        username = str(name.replace(" ", "-") + family_name.replace(" ", "-"))
        username = username.replace(" ", "-")
        email = data["ostad-email"]
        password = data["password2"]
        u = User.objects.create(
            username=username,
            first_name=name,
            last_name=family_name,
            email=email,
            is_staff=True,
        )
        u.set_password(password)
        u.save()

        education = data["ostad-level"]
        phone_number = data["ostad-local-number"]
        p = Professor.objects.create(
            p_user=u, level_of_education=education, phone_number=phone_number
        )
        p.save()

        #         # p_upload = ProfessorUpload.objects.create(
        #         #     p_professor=p,
        #         #     p_about=data["p_about"],
        #         #     p_education=data["p_education"],
        #         #     p_liking=data["p_liking"],
        #         #     p_papers_isi=data["p_papers_isi"],
        #         #     p_papers=data["p_papers"],
        #         #     p_convention_isi=data["p_convention_isi"],
        #         #     p_convention=data["p_convention"],
        #         #     p_translation=data["p_translation"],
        #         #     p_projects_pending=data["p_projects_pending"],
        #         #     p_projects_complete=data["p_projects_complete"],
        #         #     p_education_project=data["p_education_project"],
        #         #     p_projects=data["p_projects"],
        #         #     p_prizes=data["p_prizes"],
        #         # )
        #         # p_upload.save()
        messages.success(request, f"Professor {name} was added successfully")

        return redirect("index-admin")


def professor_upload_all(request):
    pp = ProfessorPost.objects.all()
    return render(request, "professor/professor-all.html", {"professor_posts": pp})


def professor_upload(request):
    if request.method == "POST":
        form = ProfessorUploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index-admin")
    else:
        p = Professor.objects.get(p_user=request.user)
        form = ProfessorUploadForm()
        return render(
            request, "professor/professor-upload.html", {"form": form, "p": p}
        )


def professor_post_create(request):
    if request.method == "POST":
        form = ProfessorPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index-admin")
    else:
        p = Professor.objects.get(p_user=request.user)
        form = ProfessorPostForm()
        return render(
            request, "professor/professor-post-create.html", {"form": form, "p": p}
        )


def professor_post_edit(request, id):
    p = Professor.objects.get(p_user=request.user)
    pp = ProfessorPost.objects.get(pk=id)
    if request.method == "POST":
        form = ProfessorPostForm(request.POST, request.FILES, instance=pp)
        if form.is_valid():
            form.save()
            return redirect("professor-all")
    else:
        form = ProfessorPostForm(instance=pp)
        return render(
            request,
            "professor/professor-post-create.html",
            {"pp": pp, "form": form, "p": p},
        )


def professor_post_delete(request, id):
    pp = ProfessorPost.objects.get(pk=id)
    pp.delete()
    return redirect("professor-all")
