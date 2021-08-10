from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models import (
    DO_NOTHING,
    BooleanField,
    CharField,
    ForeignKey,
    ImageField,
    Model,
)
from django.utils.translation import gettext_lazy as _
from django_jalali.db.models import jDateField, jDateTimeField
from jdatetime import date
from professor_app.models import Departmant

from core.utils.date_utilis import get_month_name

# DEFINE MODELS


class NewsPost(Model):
    written_by = ForeignKey(
        User, on_delete=DO_NOTHING, blank=True, null=True, editable=False
    )
    STYLES = (
        ("اخبار", "اخبار"),
        ("اطلاعیه", "اطلاعیه"),
    )
    post_style = CharField(_("نوع پست"), max_length=50, choices=STYLES, default="اخبار")
    target_dep = ForeignKey(Departmant, verbose_name=_("دانشکده"), on_delete=DO_NOTHING)
    date_created = jDateTimeField(_("تاریِخ"), auto_now_add=True)
    post_image = ImageField(
        _("عکس"), default="", upload_to="post_images/", blank=True, null=True
    )
    title = CharField(_("موضوع"), max_length=50)
    content = RichTextField(_("متن"))
    draft = BooleanField(
        verbose_name=_("پخش شود؟"),
        help_text=_("اگر تیک شود قابل مشاهده برای همه خواهد بود"),
        default=True,
    )

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "اخبار / اطلاعیه ها"
        ordering = ("-date_created",)

    def __str__(self):
        return self.title

    def get_time(self):
        # This du dad saves it with miliseconds, and so we first remove date, then milisecond
        date = str(self.date_created).split(" ")[0]
        time = str(self.date_created).split(" ")[1].split(".")[0]
        return f"{date} - {time}"


class Event(Model):
    event_date = jDateField(verbose_name=_("تاریخ رویداد"))
    time_left = jDateField(_("روز باقی مانده(تغییر ندهید)"), auto_now_add=True)
    title = CharField(verbose_name=_("موضوع"), max_length=100)
    draft = BooleanField(verbose_name=_("پخش شود؟"), default=True)

    class Meta:
        verbose_name = "رویداد"
        verbose_name_plural = "رویداد ها"
        ordering = ("-event_date",)

    def get_event_date_month(self):
        month = str(self.event_date).split("-")[1]
        month_name = get_month_name(int(month))
        return month_name

    def get_event_date_day(self):
        day = str(self.event_date).split("-")[2]
        return day

    def show_time_left(self):
        y2, y1 = int(str(self.event_date).split("-")[0]), int(str(self.time_left).split("-")[0])
        m2, m1 = int(str(self.event_date).split("-")[1]), int(str(self.time_left).split("-")[1])
        d2, d1 = int(str(self.event_date).split("-")[2]), int(str(self.time_left).split("-")[2])
        t2 = date(y2, m2, d2)
        t1 = date(y1, m1, d1)
        time_left = str(t2 - t1).split(" ")[0]

        return int(time_left)

    def __str__(self):
        return self.title


class Lecture(Model):
    written_by = ForeignKey(
        User, on_delete=DO_NOTHING, blank=True, null=True, editable=False
    )
    STYLES = (
        ("آموزش", "آموزش"),
        ("همایش", "همایش"),
    )
    lecture_type = CharField(
        _("نوع آموزش"), max_length=50, choices=STYLES, default="آموزش"
    )
    target_dep = ForeignKey(Departmant, verbose_name=_("دانشکده"), on_delete=DO_NOTHING)
    title = CharField(_("موضوع"), max_length=50)
    date_created = jDateTimeField(_("تاریِخ"), auto_now_add=True)
    post_image = ImageField(
        _("عکس"), default="", upload_to="post_images/", blank=True, null=True
    )
    content = RichTextField(_("متن"))
    draft = BooleanField(
        verbose_name=_("پخش شود؟"),
        help_text=_("اگر تیک شود قابل مشاهده برای همهخواهد بود"),
        default=True,
    )

    class Meta:
        verbose_name = "آموزش"
        verbose_name_plural = "آموزش ها / همایش ها"
        ordering = ("-date_created",)

    def __str__(self):
        return self.title

    def get_time(self):
        # This du dad saves it with miliseconds, and so we first remove date, then milisecond
        date = str(self.date_created).split(" ")[0]
        time = str(self.date_created).split(" ")[1].split(".")[0]
        return f"{date} - {time}"
