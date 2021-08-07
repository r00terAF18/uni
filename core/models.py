from datetime import date

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models import (
    DO_NOTHING,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    ForeignKey,
    ImageField,
    Model,
)
from django.utils.translation import gettext_lazy as _
from jdatetime import datetime as jdate

from core.utils.date_utilis import get_month_name

from professor_app.models import Departmant

# DEFINE MODELS


class NewsPost(Model):
    written_by = ForeignKey(User, on_delete=DO_NOTHING)
    STYLES = (
        ("اخبار", "اخبار"),
        ("اطلاعیه", "اطلاعیه"),
    )
    post_style = CharField(_("نوع پست"), max_length=50, choices=STYLES, default="اخبار")
    target_dep = ForeignKey(
        Departmant, verbose_name=_("دپارتمانت"), on_delete=DO_NOTHING
    )
    date_created = DateTimeField(_("تاریِخ"), auto_now_add=True)
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

    def convert_date(self):
        date = jdate.fromgregorian(datetime=self.date_created)
        return f"{date.day} {get_month_name(date.month)} {date.year}"

    def get_time(self):
        # This du dad saves it with miliseconds, and so we first remove date, then milisecond
        date = str(self.date_created).split(" ")[0]
        time = str(self.date_created).split(" ")[1].split(".")[0]
        return f"{date} - {time}"


class Event(Model):
    event_date = DateField(_("تاریخ رویداد"), max_length=50)
    time_left = DateField(_("روز باقی مانده(تغییر ندهید)"), auto_now_add=True)
    title = CharField(_("موضوع"), max_length=100)
    draft = BooleanField(_("پخش شود؟"), default=True)

    class Meta:
        verbose_name = "رویداد"
        verbose_name_plural = "رویداد ها"
        ordering = ("-event_date",)

    def get_event_date_month(self):
        date = jdate.fromgregorian(datetime=self.event_date)
        month_name = get_month_name(date.month)
        return month_name

    def get_event_date_day(self):
        date = jdate.fromgregorian(datetime=self.event_date)
        return date.day

    def get_time_left(self):
        # first get the diff in time, which returns a very nice string
        # but were only interested in the time, and so trim the shit down
        xxx = self.event_date - date.today()
        time_left = str(xxx).split(" ")[0]
        return time_left

    def __str__(self):
        return self.title


class Lecture(Model):
    written_by = ForeignKey(User, on_delete=DO_NOTHING)
    STYLES = (
        ("آموزش", "آموزش"),
        ("همایش", "همایش"),
    )
    lecture_type = CharField(
        _("نوع آموزش"), max_length=50, choices=STYLES, default="آموزش"
    )
    title = CharField(_("موضوع"), max_length=50)
    date_created = DateTimeField(_("تاریِخ"), auto_now_add=True)
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

    def convert_date(self):
        date = jdate.fromgregorian(datetime=self.date_created)
        return f"{date.day} {get_month_name(date.month)} {date.year}"

    def get_time(self):
        # This du dad saves it with miliseconds, and so we first remove date, then milisecond
        date = str(self.date_created).split(" ")[0]
        time = str(self.date_created).split(" ")[1].split(".")[0]
        return f"{date} - {time}"
