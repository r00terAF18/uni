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
from django_jalali.db.models import jDateTimeField
from faculty_app.models import Departmant

# DEFINE MODELS


class Lecture(Model):
    written_by = ForeignKey(
        User, on_delete=DO_NOTHING, blank=True, null=True, editable=False
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
        verbose_name_plural = "آموزش ها"
        ordering = ("-date_created",)

    def __str__(self):
        return self.title

    def get_time(self):
        # This du dad saves it with miliseconds, and so we first remove date, then milisecond
        date = str(self.date_created).split(" ")[0]
        time = str(self.date_created).split(" ")[1].split(".")[0]
        return f"{date} - {time}"
