from ckeditor.fields import RichTextField
from django.db.models import (
    CASCADE,
    DO_NOTHING,
    CharField,
    FileField,
    ForeignKey,
    ImageField,
    ManyToManyField,
    Model,
)
from django.utils.translation import gettext_lazy as _
from professor_app.models import Professor


class Departmant(Model):
    name = CharField(verbose_name=_("نام دانشکده"), max_length=50)
    image = ImageField(
        _("عکس"), default="", upload_to="departmant/", blank=True, null=True
    )
    head = ForeignKey(
        Professor,
        related_name=_("head"),
        verbose_name="رئیس دانشکده",
        on_delete=DO_NOTHING,
        blank=True,
    )
    ostads = ManyToManyField(
        Professor, related_name=_("ostads"), verbose_name=_("اساتید")
    )
    info = RichTextField(_("پیام رئیس دانشکده"))

    class Meta:
        verbose_name = "دانشکده"
        verbose_name_plural = "دانشکده ها"

    def __str__(self):
        return f"{self.name}"


class DepartmentAbstract(Model):
    dep = ForeignKey(Departmant, on_delete=CASCADE)
    name = CharField(verbose_name=_("نام"), max_length=255)

    class Meta:
        abstract = True


class DepForms(DepartmentAbstract):
    form_file = FileField(verbose_name=_("فورم"), upload_to="department/forms/")

    def __str__(self) -> str:
        return f"{self.name} - دانشکده {self.dep}"

    class Meta:
        verbose_name = _("فایل دانشکده")
        verbose_name_plural = _("فایل های دانشکذه")


class DepLab(DepartmentAbstract):
    lab_link = CharField(verbose_name=_("لینک"), max_length=255)

    def __str__(self) -> str:
        return f"{self.name} - دانشکده {self.dep}"

    class Meta:
        verbose_name = _("دانشکده آزمایشگاه")
        verbose_name_plural = _("دانشکده آزمایشگاه ها")
