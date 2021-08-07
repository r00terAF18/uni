from sidebar_app.models import Sidebar
from django.shortcuts import get_object_or_404, render

from .models import Event, NewsPost


def event_all(request):
    news_events = Event.objects.all().filter(draft=True)
    context = {"news_events": news_events}
    return render(request, "all-links-event.html", context)


def news_all(request):
    news_news = NewsPost.objects.all().filter(post_style="اخبار", draft=True)
    context = {"news_news": news_news}
    return render(request, "all-links-news.html", context)


def notif_all(request):
    news_notif = NewsPost.objects.all().filter(post_style="اطلاعیه", draft=True)
    context = {"news_notif": news_notif}
    return render(request, "all-links-notification.html", context)


def news_detail(request, id):
    news = get_object_or_404(NewsPost, id=id)
    sidebar = Sidebar.objects.all().filter(sidebar_on_page="News").first()
    print(sidebar)
    return render(request, "single-news.html", {"news": news, "sidebar": sidebar})
