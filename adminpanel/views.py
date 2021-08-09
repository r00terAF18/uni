from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def professor_login(request):
    if request.method == "POST":
        data = request.POST
        email = data["email"]
        user_wanting_login = User.objects.get(email=email)
        u = authenticate(
            request, username=user_wanting_login.username, password=data["password"]
        )
        if u is not None:
            login(request, u)
            messages.success(
                request,
                f"Professor {u.first_name} {u.last_name} logged in Successfully",
            )
            return redirect("/admin")
        else:
            messages.error(request, f"Provided Information was not correct")
    else:
        return redirect("home_view")


@login_required
def professor_logout(request):
    logout(request)
    return redirect("home_view")


# @login_required
# def list_self_posts(request):
#     student = Student.objects.get(user=request.user)
#     student_posts = StudentPost.objects.all().filter(from_student=student)
#     sp_filter = SelfPostFilter(request.GET, queryset=student_posts)
#     context = {
#         "student_posts": sp_filter.qs,
#         "filter": sp_filter,
#     }
#     return render(request, "admin_daneshjo_list.html", context)


# def list_student_posts(request):
#     students = Student.objects.all()
#     sp = StudentPost.objects.all().filter(draft=True)
#     sp_filter = StudentPostFilter(request.GET, queryset=sp)
#     context = {
#         "student_posts": sp_filter.qs,
#         # "filter": sp_filter,
#         "all_students": students,
#     }
#     return render(request, "admin_daneshjo_all_posts.html", context)


# @login_required
# def submit_student_post(request):
#     if request.method == "POST":
#         data = request.POST
#         from_student = request.user.student
#         title = data["title"]
#         content = data["content"]
#         post_image = request.FILES.get("post_image")

#         sp = StudentPost.objects.create(
#             from_student=from_student,
#             title=title,
#             content=content,
#             post_image=post_image,
#         )
#         sp.save()
#         return redirect("admin_panel:admin_daneshjo_list_self_post")
#     else:
#         form = StudentPostForm()
#         context = {"form": form}
#         return render(request, "admin_daneshjo_post.html", context)


# @login_required
# def update_post(request, id):
#     sp = StudentPost.objects.get(id=id)
#     if request.method == "POST":
#         data = request.POST
#         from_student = request.user.student
#         title = data["title"]
#         content = data["content"]
#         post_image = request.FILES.get("post_image")

#         sp.from_student = from_student
#         sp.title = title
#         sp.content = content
#         sp.post_image = post_image
#         sp.save()
#         return redirect("admin_panel:admin_daneshjo_list_self_post")
#     else:
#         form = StudentPostForm()
#         context = {
#             "form": form,
#             "sp": sp,
#         }
#         return render(request, "admin_daneshjo_post.html", context)


# def detail_sp(request, id):
#     sp = get_object_or_404(StudentPost, id=id)
#     return render(request, "single-news.html", {"news": sp})


# @login_required
# def remove_post(request):
#     if request.method == "POST":
#         StudentPost.objects.filter(id=request.POST["post_id"]).delete()
#         return redirect("admin_panel:admin_daneshjo_list_posts")
#     else:
#         pass


# def secret_register(request):
#     if request.method == "POST":
#         entered_key = str(request.POST["code"])
#         student_id = str(request.POST["student_id"])
#         student_full_name = str(request.POST["student_full_name"])
#         mail = student_id + "@spu.ac.ir"
#         student_code_meli = str(request.POST["student_code_meli"])
#         code = ""
#         with open(settings.BASE_DIR / "key.txt", "r") as f:
#             code = f.readline()
#             f.close()
#         if entered_key == str(code):
#             u = User.objects.create(
#                 username=student_id, password=student_code_meli, email=mail
#             )
#             u.set_password(student_code_meli)
#             u.save()
#             student = Student.objects.create(
#                 user=u,
#                 full_name=student_full_name,
#                 student_id=student_id,
#                 student_code_meli=student_code_meli,
#             )
#             student.save()
#             return redirect("admin_panel:admin_daneshjo_index")
#         else:
#             return redirect("home_view")
