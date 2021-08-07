from django.shortcuts import render

from core.utils.data_retriever import *

from .models import Event, Lecture, NewsPost
from adminpanel.models import UniSystem
from professor_app.models import ProfessorPost


def home_view(request):
    # Shitty way of deleting overdue Events
    possible_overdue = Event.objects.all()
    for event in possible_overdue:
        if str(event.get_time_left()) == "0:00:00" or event.get_time_left()[0] == "-":
            event.delete()

    c = retrieve_carousel()

    first_four_lectures = first_of_lectures(4, Lecture, "آموزش")
    first_four_unievents = first_of_lectures(4, Lecture, "همایش")

    first_four_news = first_of_n(4, NewsPost, "اخبار")
    first_four_info = first_of_n(4, NewsPost, "اطلاعیه")

    all_n_notification = Event.objects.all().filter(draft=True)

    # all_sp = StudentPost.objects.all().filter(draft=True)

    first_four_notification = []

    first_four_sp = []

    for n in all_n_notification.reverse():
        first_four_notification.append(n)
        if len(first_four_notification) == 3:
            break

    # for sp in all_sp:
    #     first_four_sp.append(sp)
    #     if len(first_four_sp) == 4:
    #         break

    uni_system = UniSystem.objects.all()

    context = {
        "c": c,
        "first_four_news": first_four_news,
        "first_four_info": first_four_info,
        "first_four_notification": first_four_notification,
        "first_four_sp": first_four_sp,
        "first_four_lectures": first_four_lectures,
        "first_four_unievents": first_four_unievents,
        "uni_system": uni_system,
    }
    return render(request, "index.html", context)


# def all_student_posts_index(request):
#     all_sp = StudentPost.objects.all().filter(draft=True)
#     return render(request, "all_student_posts.html", {"all_sp": all_sp})


def search_query(request):
    print(request)
    data = request.GET
    if len(data["search-bar"]) > 0:
        query = data["search-bar"]
        # thanks to django ORM and SQL, searching can be as simple as this
        n = NewsPost.objects.filter(title__contains=query)
        e = Event.objects.filter(title__contains=query)
        l = Lecture.objects.filter(title__contains=query)
        p = ProfessorPost.objects.filter(title__contains=query)

        context = {"n_filter": n, "e_filter": e, "l_filter": l, "p_filter": p, "query": query}

        return render(request, "search.html", context)
    else:
        return render(request, "search.html")


def no_access(request):
    return render(request, "404.html")
