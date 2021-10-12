from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models import (
    CASCADE,
    CharField,
    EmailField,
    ForeignKey,
    ImageField,
    Model,
    OneToOneField,
)
from django.utils.translation import gettext_lazy as _
from django_jalali.db.models import jDateTimeField


class Professor(Model):
    p_user = OneToOneField(User, on_delete=CASCADE, blank=True, editable=False)
    f_name = CharField(verbose_name=_("نام"), max_length=255)
    l_name = CharField(verbose_name=_("نام خانوادگی"), max_length=255)
    email = EmailField(verbose_name=_("ایمیل"), max_length=255)
    password = CharField(verbose_name=_("پسورد"), max_length=255, unique=True)
    image = ImageField(
        verbose_name=_("عکس"), default="", upload_to="staff/", blank=True
    )
    level_of_education = CharField(verbose_name=_("مرتبه علمی"), max_length=50)
    phone_number = CharField(verbose_name=_("شماره داخلی"), max_length=15, blank=True)

    class Meta:
        verbose_name = "استاد"
        verbose_name_plural = "اساتید"

    def __str__(self):
        return f"{self.f_name}"


class ProfessorPost(Model):
    professor = ForeignKey(Professor, on_delete=CASCADE)
    title = CharField(verbose_name=_("تایتل پست"), max_length=255)
    image = ImageField(
        verbose_name=_("عکس"), upload_to="professor_post/", blank=True, null=True
    )
    content = RichTextField("متن")
    date_created = jDateTimeField(_("تاریِخ"), auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)

    def get_time(self):
        # This du dad saves it with miliseconds, and so we first remove date, then milisecond
        date = str(self.date_created).split(" ")[0]
        time = str(self.date_created).split(" ")[1].split(".")[0]
        return f"{date} - {time}"

    class Meta:
        verbose_name = _("پست استاد")
        verbose_name_plural = _("پست اساتید")


class ProfessorUpload(Model):
    p_professor = ForeignKey(Professor, on_delete=CASCADE)
    p_about = RichTextField("توضیحات", blank=True)
    p_education = RichTextField("سوابق تحصیلی", blank=True)
    p_liking = RichTextField("زمینه های تحقیقاتی مورد علاقه", blank=True)
    p_papers_isi = RichTextField(
        "مقالات چاپ شده در نشریات معتبر علمی- پژوهشی بین المللی و ISI", blank=True
    )
    p_papers = RichTextField("مقالات چاپ شده در نشریات معتبر داخلی", blank=True)
    p_convention_isi = RichTextField("همایش های بین المللی", blank=True)
    p_convention = RichTextField("همایش های ملی و منطقه ای", blank=True)
    p_translation = RichTextField("تالیف و ترجمه کتاب", blank=True)
    p_projects_pending = RichTextField("طرح های تحقیقاتی در دست اجرا", blank=True)
    p_projects_complete = RichTextField("طرح های تحقیقاتی خاتمه یافته", blank=True)
    p_education_project = RichTextField(
        "راهنمایی و مشاوره پروژه های کارشناسی، پایان نامه های کارشناسی ارشد و رساله های دکتری",
        blank=True,
    )
    p_projects = RichTextField("فعالیتهای اجرایی", blank=True)
    p_prizes = RichTextField("جوایز و افتخارات", blank=True)

    def __str__(self) -> str:
        return str(self.p_professor)

    class Meta:
        verbose_name = _("درباره استاد")
        verbose_name_plural = _("درباره اساتید")
