from django.db.models import BooleanField, CharField, Model
from django.utils.translation import gettext_lazy as _
from django_jalali.db.models import jDateField
from jdatetime import date
from news_app.utils.date_utilis import get_month_name

# DEFINE MODELS


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
        y2, y1 = int(str(self.event_date).split("-")[0]), int(
            str(self.time_left).split("-")[0]
        )
        m2, m1 = int(str(self.event_date).split("-")[1]), int(
            str(self.time_left).split("-")[1]
        )
        d2, d1 = int(str(self.event_date).split("-")[2]), int(
            str(self.time_left).split("-")[2]
        )
        t2 = date(y2, m2, d2)
        t1 = date(y1, m1, d1)
        time_left = str(t2 - t1).split(" ")[0]

        return int(time_left)

    def __str__(self):
        return self.title
